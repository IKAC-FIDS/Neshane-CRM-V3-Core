# V3-LOCAL-INFRA-004 — residual limitations

These limitations are retained and not waived by the development-only acceptance
recommendation.

1. **Development-only / synthetic-data scope.** All configuration and runtime
   evidence uses synthetic, task-owned data. Nothing here validates real customer,
   tenant, production or personal data handling.

2. **Loopback service egress.** Because Docker Desktop suppresses host port
   publication on `internal: true` networks, published development services use
   non-internal networks. Container egress isolation is therefore **not provided**
   for published services; segmentation, loopback binds, no-privileged posture and
   resource limits remain the security boundary.

3. **Redis remains internal and unpublished.** Redis has no host port and no other
   configured peer; its trust boundary is its own internal network and it must not
   receive real session/cache/tenant data.

4. **No hostile-host isolation.** Containers run on a trusted local Docker Desktop
   host; the configuration does not and cannot establish resistance to a hostile
   shared host, hypervisor, or privileged administrator.

5. **No power-loss durability.** Persistence evidence is limited to process
   restarts on the trusted host; it does not establish power-loss, media-failure or
   crash-consistency durability.

6. **No complete DLP guarantee.** The synthetic telemetry filters minimize common
   attribute/status/description fields and drop span events, but they are not an
   exhaustive data-loss-prevention system and must not receive production data even
   with the synthetic marker.

7. **No production security readiness.** Nothing here constitutes Security Sign-off,
   production IAM, production RLS, credential lifecycle acceptance, or production
   observability architecture acceptance.

8. **SeaweedFS EXPERIMENTAL.** The experimental S3 mini instance is dev-only; OD-017
   (object storage provider) remains unresolved.

9. **Temporary preservation snapshot limitation.** The original checkout's temporary
   preservation snapshot helper files (raw index and working-tree copies) were
   partially removed by environment temp cleanup; the original repositories remain
   byte-intact and the recoverable staged/unstaged patches and manifest remain.

10. **Image references are identity correspondence, not attestation.** Digest
    resolution over HTTPS establishes image identity for reproducibility, not
    publisher attestation, vulnerability-free status or supply-chain acceptance.
