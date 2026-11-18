#!/usr/bin/env escript
%% Synthetic task-local AMQP 0-9-1 handshake. Credentials stay in container env.
main(_) ->
    try run_checks()
    catch Class:Reason ->
        io:format("AMQP_PROBE_FAILED class=~p stage=~p reason=~p~n", [Class,get(stage),safe_reason(Reason)]),
        halt(1)
    end.

safe_reason({badmatch,{error,A}}) when is_atom(A) -> A;
safe_reason({badmatch,<<10:16,50:16,Code:16,_/binary>>}) -> {connection_close,Code};
safe_reason({badmatch,<<Class:16,Method:16,_/binary>>}) -> {unexpected_method,Class,Method};
safe_reason({badmatch,A}) when is_atom(A) -> A;
safe_reason(_) -> redacted_error.

run_checks() ->
    User = list_to_binary(os:getenv("RABBITMQ_DEFAULT_USER")),
    Password = list_to_binary(os:getenv("RABBITMQ_DEFAULT_PASS")),
    put(stage, valid_authentication),
    true = login(User, Password),
    put(stage, invalid_authentication),
    rejected = login(User, <<"invalid-synthetic-password">>),
    io:format("AMQP_VALID_AND_INVALID_PASS~n").

short(B) -> <<(byte_size(B)):8, B/binary>>.
long(B) -> <<(byte_size(B)):32, B/binary>>.
send_frame(S, B) -> gen_tcp:send(S, <<1:8, 0:16, (byte_size(B)):32, B/binary, 206:8>>).
recv(S) ->
    case gen_tcp:recv(S, 7, 5000) of
        {ok, <<1:8, 0:16, Size:32>>} ->
            {ok, Body} = gen_tcp:recv(S, Size, 5000),
            {ok, <<206:8>>} = gen_tcp:recv(S, 1, 5000),
            Body;
        {error, closed} -> closed
    end.

login(User, Password) ->
    Phase = get(stage),
    {ok, S} = gen_tcp:connect("127.0.0.1", 5672, [binary, {active,false}], 5000),
    put(stage,{Phase,protocol_start}),
    ok = gen_tcp:send(S, <<"AMQP",0,0,9,1>>),
    <<10:16,10:16,_/binary>> = recv(S),
    Cap = <<(short(<<"authentication_failure_close">>))/binary, $t, 1>>,
    Props = <<(short(<<"capabilities">>))/binary, $F, (long(Cap))/binary>>,
    Response = <<0,User/binary,0,Password/binary>>,
    ok = send_frame(S, <<10:16,11:16,(long(Props))/binary,(short(<<"PLAIN">>))/binary,
                   (long(Response))/binary,(short(<<"en_US">>))/binary>>),
    put(stage,{Phase,start_ok_response}),
    Result = case recv(S) of
        <<10:16,30:16,_/binary>> ->
            ok = send_frame(S, <<10:16,31:16,0:16,131072:32,0:16>>),
            ok = send_frame(S, <<10:16,40:16,(short(<<"neshane_dev">>))/binary,0,0>>),
            put(stage,{Phase,vhost_open_response}),
            <<10:16,41:16,_/binary>> = recv(S),
            true;
        <<10:16,50:16,403:16,_/binary>> -> rejected;
        <<10:16,50:16,530:16,_/binary>> -> rejected;
        closed -> rejected
    end,
    gen_tcp:close(S),
    Result.
