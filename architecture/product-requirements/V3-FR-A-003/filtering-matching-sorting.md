# Filtering, matching, sorting and pagination

- D02–D03: general search and combined filtering over authorized fields. AND/OR grouping, free-text field precedence and default empty query remain OPEN.
- D04: name exact, prefix, contains; literal examples `Alpha` exact matches `Alpha`, prefix matches `Alpha Test`, contains matches `Test Alpha Group`. These are documentary examples using synthetic data, not an algorithm decision.
- D05: official identifier exact only, with applicable type/issuer context; no prefix, contains, fuzzy match or enumeration bypass.
- D06: Persian/English support with character and digit normalization; exact normalization equivalences, Unicode/case/diacritic/whitespace and identifier-specific transforms require explicit approval and must not merge distinct identities. Do not invent transliteration or fuzzy rules.
- D08–D09: name, created time, last modification; default last modification descending. Stable tie-break, null ordering, locale collation and consistency under concurrent updates remain OPEN; do not silently choose cursor or offset.
- D10: page sizes 20/50/100, no unbounded listing. Exact default size and invalid-value response remain OPEN. Counts, if exposed, and navigation must be computed against authorized matched records only. No hidden-record leakage via counts or empty pages.
- D14: return latest valid recorded state; no silently stale substitute or offline result. Freshness mechanism, maximum lag, snapshot semantics and concurrent update paging guarantees remain OPEN.

Search mechanism OD-018, API exposure OD-007, query contract, indexing, numeric performance targets and storage selection remain outside this task. All unresolved observable behavior blocks affected implementation.
