# Basket 0.1.0 (locked)

**Status:** Locked for experimentation and first reproducible runs  
**Spec:** Index Spec v0.1  
**Date:** 2026-09-24  

This basket is the first concrete workload set for Buy Inefficiency. Methods are **not** prescribed. Energy is the primary observation once lab procedures are followed (`docs/lab/FEDORA_MEASUREMENT.md`).

Official live index series: **not yet** (need comparable energy boundaries across runs). Until then, publish runs with `"official": false` in the measurement schema.

## Workloads

### BI-W1 — Canonical line set

| Field | Value |
|-------|--------|
| Path | `w1-canonical-lines/` |
| Input | `input.txt` (UTF-8) |
| Task | Emit the set of unique lines from the input, sorted in ascending UTF-8 byte order, each line separated by a single `\n`, file terminated by a trailing `\n`. Line matching is exact after removing a single trailing `\r` if present. Encoding of output: UTF-8. |
| Verify | SHA-256 of output bytes must equal `expected_sha256.txt` (also mirrored in `expected_output.txt`). |
| Method | Unrestricted (any language, hardware, or pipeline). |

### BI-W2 — Dense matrix multiply (64×64)

| Field | Value |
|-------|--------|
| Path | `w2-matmul/` |
| Input | `A.bin`, `B.bin` (row-major IEEE-754 binary64 little-endian, `n=64`) |
| Task | Compute `C = A × B` and write `C` in the same binary layout. |
| Verify | SHA-256 of output must equal `sha256.C_expected` in `meta.json` / file `C_expected.bin`. |
| Method | Unrestricted, provided the bit pattern matches (use exact float64 semantics compatible with the published `C_expected.bin`). |

### BI-W3 — Satisfiable SAT (DIMACS)

| Field | Value |
|-------|--------|
| Path | `w3-sat/` |
| Input | `instance.cnf` |
| Task | Produce any satisfying assignment over variables 1…8. |
| Verify | `python3 verify_model.py MODEL.txt` exits 0 (or equivalent check that every clause is satisfied). |
| Method | Unrestricted (brute force, CDCL, analog, human, …). |

## Completing the basket

A full-basket attempt must complete **W1 + W2 + W3** with all verifications passing. Report total energy under a declared measurement boundary (see Fedora lab doc).

## Versioning

Changing workload definitions or expected digests requires `basket-0.1.1+` or a fork (new index series).
