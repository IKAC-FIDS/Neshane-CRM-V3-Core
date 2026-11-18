# V3-LOCAL-INFRA-001 — development baseline hardening report

## Authorization and original preservation

Authority source: current explicit owner conversation, Task ID
`V3-LOCAL-INFRA-001`, Title `Local-Infra Development Baseline Hardening`, working
branch `codex/v3-local-infra-001`; all prior scope restrictions retained. The exact
scope authorizes isolated development/synthetic configuration correction and static
validation only, not runtime, production, staging, commit or push. Initial local
preservation/authorization observation: `2026-11-18T13:45:03.0450796+03:30`; this is
a recording observation, not an invented authority issuance time or Gate decision.

Original checkout: `E:\Neshane-CRM-V3`, branch
`codex/v3-024-root-preservation`, HEAD
`c3926e6a8c9847281d49987abdbafbbced562dbb`. Its eight staged additions are empty
placeholders; six have unstaged content and two SeaweedFS files are untracked.
No original file/index layer is edited. Actual `.env` remains ignored in place;
it is neither read nor copied, and is intentionally excluded from the non-secret
snapshot. Its values are not claimed backed up by this Task.

Recoverable non-secret snapshot:
`C:\Users\user\AppData\Local\Temp\opencode\V3-LOCAL-INFRA-001\`.
It contains `preservation.json`, `original-index.bin`, separate binary/full-index
`staged.patch` and `unstaged.patch`, eight working-tree file copies and two separate
untracked copies. Hash/length equality was verified BEFORE corrections. The raw
index is preservation evidence, not a file to apply blindly to another checkout.
The verifier also checks protected repository HEADs/branches, statuses, staged and
unstaged diffs and tracked bytes. No Backend/Frontend work or evidence is changed.

Protected Backend was `abd76d821c98e1fe10fe2d6c2c1772b0df7641e7`, clean;
Frontend `faa563f8f5c3bda25c3e5f40c7a8688c1bc245e7`, clean. Authoritative Root Main
was clean at `094c966de745285bd5a8d1975312eb06d930d4a8`.

## Isolated workspace and file scope

Created `E:\Neshane-CRM-V3-V3-LOCAL-INFRA-001` and
`codex/v3-local-infra-001` directly from authoritative Main
`094c966de745285bd5a8d1975312eb06d930d4a8`. Worktree creation necessarily registers
the new branch/worktree in shared Git metadata; it does not modify the original
checkout's files, HEAD, branch or index. No source checkout synchronization occurs.

Only the six non-empty intended Local-Infra worktree files were transferred from
the VERIFIED preservation copy. No actual env, staged placeholder or diagnostic
file was transferred. Corrections are confined to this worktree's `Local-Infra/`:

```text
.env.example
.gitattributes
.gitignore
README.md
compose.yaml
compose.seaweedfs.yaml
configuration-sources.md
image-references.json
postgres/10-development-role.sh
rabbitmq/rabbitmq.conf
observability/grafana-datasources.yaml
observability/otel-collector.yaml
observability/prometheus.yml
observability/tempo.yaml
runtime-validation-plan.md
Validate-DevelopmentBaseline.ps1
validation-report.md
```

Generated synthetic input files/YAML wrappers/results live only in ignored
`.validation/`. Source/registry snapshots and original-preservation tooling remain
in the external local evidence directory, not in the original checkout or Git index.

## Material corrections

- Nine publisher/official registry image references actually resolved over HTTPS,
  index digests checked, linux/amd64 metadata read; no guessed versions/digests.
  Exact PostgreSQL 17.12, Redis 7.4.12 and RabbitMQ 4.2.9 tags confirmed after
  inspecting version metadata. Mailpit latest replaced by verified v1.34.0.
  Original SeaweedFS digest retained; source revision/4.50 label identified.
- No fixed container names, configurable project/ports, loopback publication,
  separate internal networks, bounded CPU/memory/PIDs/log files, restart=no and
  no-new-privileges. No host networking/socket/privileged container. Stable RabbitMQ
  container-local hostname preserves its own development node identity.
- Fresh-volume-only restricted PostgreSQL app identity distinct from bootstrap
  superuser; TCP authenticated app readiness, no product schema/migration/RLS.
- Redis unpublished/isolated, no product cache/session/tenant policy. RabbitMQ
  development management tag/vhost and stronger diagnostics, no product topology.
- SeaweedFS explicit opt-in Compose file; only S3 localhost publication, exact
  pinned-source flags/env reviewed, unused experimental services/telemetry disabled.
- Collector synthetic-only filtered/minimized metrics/traces, no logs/debug export,
  bounded retries/queue and internal health endpoint. Native OTTL compilation is
  unexecuted, and the synthetic marker is not security identity or full DLP.
- Prometheus/Grafana readiness and healthy dependency where available; internal
  Tempo, development retention, disabled automatic Grafana plugins/analytics and
  bounded Mailpit retention. No fabricated shell-based health checks in images
  without a verified probe. Not complete application monitoring.
- Placeholder template, credential/volume initialization semantics, LF attributes,
  explicit future-only startup/shutdown, safe non-destructive cleanup guidance and
  proposed runtime validation plan documented.

## Commands and observed static results

Executed from the isolated Root (paths below are exact):

```powershell
docker.exe compose version
& ./Local-Infra/Validate-DevelopmentBaseline.ps1
& 'C:/Users/user/AppData/Local/Temp/opencode/V3-LOCAL-INFRA-001/Preserve-Original.ps1' -Verify
```

Compose version: `v2.40.3-desktop.1`. Static validator result:
**PASS — STATIC CHECKS ONLY**. The script invokes only Compose `config` commands,
never up/run/start/exec/pull/build or a native infrastructure program. It uses a
cleared child environment, empty Docker config and explicit synthetic env-file;
expanded models are neither printed nor saved.

Observed static accounting: 6 YAML documents, 2 Compose models (8 base / 9 with
experiment), 21 template variables, 11 required-variable rejection checks, 9 pinned
image references, 10 localhost port publications, 6 Docker health checks, 6 internal
networks, 8 persistent volumes and 6 read-only scoped bind mounts. Base config
also succeeds without the four experimental credentials. All non-secret files
undergo heuristic credential scanning, non-empty/temp-file checks and individual
Git no-index whitespace checks without staging. The metadata lock separately
matched all nine actual registry observations.

`Local-Infra/.validation/static-results.json` contains current input hashes/counts
and explicit unexecuted native/runtime checks; it is local ignored evidence, not
a production or Gate acceptance. Rerun the static validator after document changes.

### Authoring/tooling failures and corrections

- Python/PyYAML was unavailable (`ModuleNotFoundError`); no dependency was installed.
  YAML parsing instead uses the installed Compose YAML parser via x-* wrappers.
- Initial registry tooling incorrectly used an unsupported Invoke-RestMethod
  `-AsHashtable` option. It was corrected to explicit JSON conversion; all nine
  metadata lookups were rerun successfully. No failed lookup is called verified.
- Guessed upstream Tempo/SeaweedFS source paths returned 404. Actual tag/revision
  paths were discovered and reviewed; no absent source was reconstructed.
- Initial static runs stopped on Windows no-index line-ending warnings, first for
  the template and then transferred YAML. Checks now inspect LF source bytes with
  command-local autocrlf=false (no persistent Git setting change), and copied YAML
  was normalized only in the isolated workspace. Whitespace checks remain enabled.

Network activity was read-only anonymous Docker Hub token/manifest/config JSON,
GitHub source/release metadata, and official documentation over normal HTTPS.
No image layer, installer, executable dependency, workload or container was pulled
or executed. Static PASS is not native config validity, image vulnerability scan,
publisher attestation, health observation or runtime enforcement evidence.

## Governance and stop

No Root ADR, standard, shared guidance, authority record or original evidence is
modified. No governance synchronization is claimed. G-RUNTIME BLOCKED; FE-BE and
AUTH/IAM authorization PENDING; OD-013/014/015/017 OPEN; offline PROHIBITED;
GS-01/GS-04 retained. Fresh restricted dev credentials do not establish product
IAM, RLS, credential lifecycle, migration ownership or accepted Runtime isolation.

Remaining gaps and exact proposed future startup/shutdown commands are in README;
native config checks, live readiness, authentication/permissions, resource behavior,
retention, telemetry minimization and experimental S3 checks require the separately
authorized `runtime-validation-plan.md`. No destructive cleanup is performed or
authorized. All task files remain unstaged/uncommitted. STOP after static validation.
