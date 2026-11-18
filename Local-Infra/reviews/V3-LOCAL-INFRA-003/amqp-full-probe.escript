#!/usr/bin/env escript
%%! -noshell
%% V3-LOCAL-INFRA-003: verified AMQP 0-9-1 client (wire-format checked against
%% rabbitmq-server v4.2.9 rabbit_framing). Uses only the image's Erlang runtime.
%% Credentials/vhost come from the container environment; never printed.
-module(amqp_full_probe).
-export([main/1]).

-define(FRAME_END, 206).
-define(CH_MAX, 2047).   %% RabbitMQ 4.x rejects channel_max=0 (unlimited).

short(B)  -> <<(byte_size(B)):8, B/binary>>.
longstr(B) -> <<(byte_size(B)):32, B/binary>>.

send(Sock, Type, Channel, Body) ->
    ok = gen_tcp:send(Sock, <<Type:8, Channel:16, (byte_size(Body)):32, Body/binary, ?FRAME_END:8>>).

method(Sock, Channel, Class, Method, Fields) ->
    send(Sock, 1, Channel, <<Class:16, Method:16, Fields/binary>>).

recv_frame(Sock) ->
    case gen_tcp:recv(Sock, 7, 5000) of
        {ok, <<Type:8, Channel:16, Size:32>>} ->
            case gen_tcp:recv(Sock, Size, 5000) of
                {ok, Body} ->
                    case gen_tcp:recv(Sock, 1, 5000) of
                        {ok, <<?FRAME_END:8>>} -> {Type, Channel, Body};
                        E1 -> E1
                    end;
                E2 -> E2
            end;
        E3 -> E3
    end.

recv_method(Sock, Class, Method) ->
    case recv_frame(Sock) of
        {1, _Ch, <<Class:16, Method:16, Rest/binary>>} -> Rest;
        {1, _Ch, <<C1:16, M1:16, _/binary>>} -> {unexpected_method, C1, M1};
        {error, closed} -> closed;
        R1 -> R1
    end.

connect() ->
    case gen_tcp:connect("127.0.0.1", 5672, [binary, {active, false}], 5000) of
        {ok, S} -> ok = gen_tcp:send(S, <<"AMQP",0,0,9,1>>), {ok, S};
        C1 -> C1
    end.

start_ok_fields(User, Password) ->
    Cap = <<(short(<<"authentication_failure_close">>))/binary, $t, 1>>,
    Props = <<(short(<<"capabilities">>))/binary, $F, (longstr(Cap))/binary>>,
    Response = <<0, User/binary, 0, Password/binary>>,
    <<(longstr(Props))/binary, (short(<<"PLAIN">>))/binary, (longstr(Response))/binary, (short(<<"en_US">>))/binary>>.

handshake(Sock, User, Password, Vhost) ->
    case recv_method(Sock, 10, 10) of
        _StartMeta when is_binary(_StartMeta) -> ok;
        HS -> {closed, {no_start, HS}}
    end,
    ok = method(Sock, 0, 10, 11, start_ok_fields(User, Password)),
    case recv_method(Sock, 10, 30) of
        <<ServerChanMax:16, ServerFrameMax:32, ServerHeartbeat:16>> ->
            ChanMax = case ServerChanMax of 0 -> ?CH_MAX; _ -> min(ServerChanMax, ?CH_MAX) end,
            FrameMax = case ServerFrameMax of 0 -> 131072; _ -> min(ServerFrameMax, 131072) end,
            ok = method(Sock, 0, 10, 31, <<ChanMax:16, FrameMax:32, ServerHeartbeat:16>>),
            ok = method(Sock, 0, 10, 40, <<(short(Vhost))/binary, 0, 0>>),
            case recv_method(Sock, 10, 41) of
                KnownHosts when is_binary(KnownHosts) -> ok;
                H1 -> {closed, {open_failed, H1}}
            end;
        {unexpected_method, C2, M2} -> {closed, {unexpected_tune_reply, C2, M2}};
        closed -> {closed, during_tune};
        H2 -> {closed, H2}
    end.

roundtrip(Sock, Queue, Payload) ->
    ok = method(Sock, 1, 20, 10, <<0:8>>),
    case recv_method(Sock, 20, 11) of
        <<_ChLen:32, _/binary>> -> ok;
        R2 -> throw({channel_open_failed, R2})
    end,
    ok = method(Sock, 1, 50, 10, <<0:16, (short(Queue))/binary, 2:8, 0:32>>),
    case recv_method(Sock, 50, 11) of
        <<_QLen:8, _/binary>> -> ok;
        R3 -> throw({queue_declare_failed, R3})
    end,
    ok = method(Sock, 1, 60, 40, <<0:16, 0:8, (short(Queue))/binary, 0:8>>),
    BodySize = byte_size(Payload),
    %% content header: class=60, weight=0, body_size, property flags, properties.
    %% AMQP 0-9-1 property-flags are MSB-first: delivery-mode = bit 12 = 0x1000.
    HeaderBody = <<60:16, 0:16, BodySize:64, 16#1000:16, 2:8>>,
    ok = send(Sock, 2, 1, HeaderBody),
    ok = send(Sock, 3, 1, Payload),
    ok = method(Sock, 1, 60, 70, <<0:16, (short(Queue))/binary, 0:8>>),
    DeliveryTag = case recv_method(Sock, 60, 71) of
        <<DT:64, _Redelivered:8, _/binary>> -> DT;
        R4 -> throw({get_failed, R4})
    end,
    {2, 1, <<60:16, _W:16, GotSize:64, _/binary>>} = recv_frame(Sock),
    {3, 1, Got} = recv_frame(Sock),
    true = (GotSize == byte_size(Got)),
    ok = method(Sock, 1, 60, 80, <<DeliveryTag:64, 0:8>>),
    {ok, Got}.

main(_) ->
    User = list_to_binary(os:getenv("RABBITMQ_DEFAULT_USER")),
    Password = list_to_binary(os:getenv("RABBITMQ_DEFAULT_PASS")),
    Vhost = <<"neshane_dev">>,
    Queue = list_to_binary("v3li003-amqp-" ++ integer_to_list(erlang:phash2(os:system_time(), 100000))),
    Payload = <<"v3li003-synthetic-amqp-message">>,
    put(stage, connect),
    {ok, S} = connect(),
    put(stage, valid_handshake),
    ok = handshake(S, User, Password, Vhost),
    put(stage, roundtrip),
    {ok, Got} = roundtrip(S, Queue, Payload),
    true = (Got == Payload),
    gen_tcp:close(S),

    put(stage, invalid_password),
    {ok, S2} = connect(),
    _ = recv_method(S2, 10, 10),
    ok = method(S2, 0, 10, 11, start_ok_fields(User, <<"invalid-synthetic-password">>)),
    Reject1 = case recv_method(S2, 10, 50) of
        <<403:16, _/binary>> -> invalid_password_rejected;
        <<CodeA:16, _/binary>> -> {unexpected_close_code, CodeA};
        N1 -> {unexpected, N1}
    end,
    gen_tcp:close(S2),

    put(stage, invalid_vhost),
    {ok, S3} = connect(),
    _ = recv_method(S3, 10, 10),
    ok = method(S3, 0, 10, 11, start_ok_fields(User, Password)),
    Reject2 = case recv_method(S3, 10, 30) of
        <<SC:16, SF:32, SH:16>> ->
            ok = method(S3, 0, 10, 31, <<(min(SC,?CH_MAX)):16, (min(SF,131072)):32, SH:16>>),
            ok = method(S3, 0, 10, 40, <<(short(<<"nonexistent-vhost">>))/binary, 0, 0>>),
            case recv_method(S3, 10, 50) of
                <<530:16, _/binary>> -> invalid_vhost_rejected;
                <<CodeB:16, _/binary>> -> {unexpected_close_code, CodeB};
                N2 -> {unexpected, N2}
            end;
        N3 -> {tune_failed, N3}
    end,
    gen_tcp:close(S3),

    io:format("AMQP_FULL_PASS payload_matches=~p reject_invalid_password=~p reject_invalid_vhost=~p~n",
              [Got == Payload, Reject1, Reject2]),
    case {Got == Payload, Reject1, Reject2} of
        {true, invalid_password_rejected, invalid_vhost_rejected} -> halt(0);
        _ -> halt(1)
    end.
