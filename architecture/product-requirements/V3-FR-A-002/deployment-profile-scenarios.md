# Deployment-profile scenarios — V3-FR-A-002

FR-BJ-001 applies to all three profiles with compatible semantics and independent evidence. No runtime behavior verified or authorized.

| Profile | Customer Master considerations | Boundary |
| --- | --- | --- |
| Shared SaaS | Shared tenant-aware persistence: validated Context, owning-Domain authorization, tenant constraints, RLS, non-bypass roles | multi-tenant cells; no cross-tenant access |
| Dedicated Managed | Physical dedication plus validated Context and Domain authorization | dedicated placement; no universal Domain authority |
| Dedicated Sovereign | Local Customer Domain authority; local Audit; no mandatory synchronous Central dependency | locally authoritative |

Common: stable non-topology-encoding Tenant identity; validated Context; owning-Domain final authorization; durable Audit; fail closed. Offline continuation PROHIBITED; Full Air Gap remains OD-001 pending.

No profile scenario executed; requirement statements only.
