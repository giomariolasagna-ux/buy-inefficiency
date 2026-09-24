# Basket proposals (candidates — not normative)

These are **discussion starters** for a future `basket-0.1.0`. They are **not** locked into Index Spec v0.1.

Selection principles:

1. Result must be **verifiable** without prescribing the algorithm.
2. Prefer workloads where **energy** (not only latency) is a meaningful differentiator.
3. Prefer tasks that can be run on diverse hardware (CPU, GPU, ASIC, novel substrates) in principle.
4. Avoid single-vendor benchmarks as the whole basket.

## Candidate themes

| ID | Theme | Why it might belong | Open questions |
|----|--------|---------------------|----------------|
| W1 | Deterministic data transform | Easy verification (hash/checksum of output) | Exact corpus + schema TBD |
| W2 | Exact combinatorial search with checkable witness | Method-agnostic; verification is a witness check | Problem family + size class TBD |
| W3 | Numerical solve with tolerance | Allows analog / approximate hardware if verification allows | Stability of energy vs precision TBD |
| W4 | Compression / decompression round-trip | Clear verify; energy-sensitive | Dataset licensing TBD |
| W5 | Inference-style workload with fixed I/O contract | Relevant to modern compute; easy to game — needs care | Model-agnostic I/O contract TBD |

## Explicitly deferred

- Training huge models end-to-end (too heavy / hard to standardize early)
- Vendor-only closed benchmarks
- Anything that cannot be verified independently

## How to propose

Use the GitHub issue template **Workload proposal**.
