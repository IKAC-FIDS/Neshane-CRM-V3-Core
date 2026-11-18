# V3-LOCAL-INFRA-005 — baseline count reconciliation

## Finding

The earlier review labels reported "17 original artifacts, 13 byte-identical, and
5 modified", which sums to `13 + 5 = 18`, one more than the 17-file baseline.

## Correction

The verified baseline is **17 files total**:

- **12 byte-identical** to the V3-LOCAL-INFRA-001 baseline.
- **5 modified** in V3-LOCAL-INFRA-003:
  1. `observability/otel-collector.yaml` (filter Advanced-OTTL correction)
  2. `compose.yaml` (`internal: true` network correction)
  3. `compose.seaweedfs.yaml` (experimental network correction)
  4. `Validate-DevelopmentBaseline.ps1` (network invariant + reviews exclusion)
  5. `README.md` (networking documentation)

`12 + 5 = 17`. The "13 byte-identical" figure was a one-file overcount in the
report label only; the actual verification checked the 12 unchanged files and
passed. No file is missing, duplicated, or outside the baseline set.

## Source

`../V3-LOCAL-INFRA-003/predecessor-hashes.json` lists exactly 17 baseline entries;
the changed-five set is documented in
`../V3-LOCAL-INFRA-003/configuration-change-matrix.json`. This reconciliation is
recorded as a correction without rewriting any historical observation.
