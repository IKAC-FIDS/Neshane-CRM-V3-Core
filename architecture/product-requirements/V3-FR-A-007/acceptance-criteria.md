# Canonical acceptance criteria and examples

| Criterion | Candidate evidence | Status |
|---|---|---|
| V3-FR-A-007-AC-01 | 19-file set and manifest | Candidate integrity checked; owner review pending |
| V3-FR-A-007-AC-02 | Trace matrix and decision ledger | Group-level trace; exact operation mapping review pending |
| V3-FR-A-007-AC-03 | Eight-gap ledger and operation catalog | Bounded dispositions; OPEN residuals |
| V3-FR-A-007-AC-04 | Synthetic examples | NOT EXECUTED |
| V3-FR-A-007-AC-05 | README and blockers | Scope maintained; no Gate change |

- EX-01: Valid active member signs in → valid Context only after validation. NOT EXECUTED.
- EX-02: No active Membership → no operational access. NOT EXECUTED.
- EX-03: Switch valid destination → new Context. NOT EXECUTED.
- EX-04: Switch invalid destination → deny. NOT EXECUTED.
- EX-05: Membership revoked during Session → deny affected Tenant at approved revalidation point. NOT EXECUTED.
- EX-06: Forged Context → deny. NOT EXECUTED.
- EX-07: Cross-Tenant request → deny without leakage. NOT EXECUTED.
- EX-08: Authorization outage → fail closed. NOT EXECUTED.
- EX-09: Cell routing failure → no invalid fallback. NOT EXECUTED.
- EX-10: Recovery → revalidate security state. NOT EXECUTED.
- EX-11: Platform admin without Domain grant → deny business access. NOT EXECUTED.
- EX-12: Offline request → deny. NOT EXECUTED.
- EX-13: Sovereign local authority without Central → local validation, not offline bypass. NOT EXECUTED.
- EX-14: Mandatory Audit failure → no bypass. NOT EXECUTED.
- EX-15: Stale/revoked Session or Context → deny according to approved freshness policy. NOT EXECUTED.

Exact approved actor, resource, Tenant and profile bindings remain OPEN. Independent profile evidence required; no scenario passed by documentary review.

