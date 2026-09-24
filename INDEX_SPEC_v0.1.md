# Buy Inefficiency — Index Specification v0.1

**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-24  
**License:** CC BY 4.0  

This document defines a public, versioned specification for an index of computational efficiency: the evolution of energy required to correctly complete a fixed basket of computational workloads, without prescribing the computational method. Forks create new indices and do not rewrite the original history. This specification does not define a token or any economic exposure mechanism.

---

## 1. Purpose

Define a public, versioned specification that makes it possible to:

1. Declare a **basket** of comparable computational workloads.
2. Measure the **energy** required to complete them correctly.
3. Build a **time series** of efficiency on that basket, independent of the technology used.
4. Allow **adoption** and **forks** without a central authority.

In this specification, progress in computing is not only an increase in available power, but also a reduction in the physical resources (especially energy) needed to obtain the same verifiable results.

## 2. Scope and non-goals

### In scope

- Definitions of workload, basket, verification, and energy measurement boundaries.
- Versioning and fork rules.
- Transparency and reproducibility requirements.

### Non-goals (v0.1)

- Not defining a token, tokenomics, an on-chain oracle, or an economic exposure mechanism.
- Not claiming a universal, final measure of computational efficiency.
- Not producing vendor or architecture rankings as a primary goal.
- Not fixing in v0.1 the concrete workload list (TBD) or full lab details (TBD).

## 3. Definitions

| Term | Definition |
|------|------------|
| **Workload** | A computational job with specified inputs, required result, and verification conditions. The solution method is not prescribed. |
| **Basket** | A versioned set of workloads that is the unit of measurement for the index. |
| **Verification** | The procedure that decides whether a result is correct relative to the workload specification. |
| **Energy measurement boundary** | The physical/logical boundary within which energy associated with running the basket is accounted for (operational detail TBD). |
| **Run** | An attempt to complete (part of) a basket on a given system, with energy and verification logs. |
| **Efficiency observation** | Measured energy (within declared boundaries) to correctly complete the basket, or a declared subset, in a valid run. |
| **Index series** | A published time sequence of observations (or aggregates) for a given basket + protocol version. |
| **Fork** | A derived specification (modified basket and/or protocol) that constitutes a **new** index with its own historical series. |

## 4. Basket requirements

A conforming basket must:

1. Be **public** (text and required artifacts available).
2. List each workload with:
   - a stable identifier;
   - a description;
   - inputs (or an input generator) that are deterministic or sampled with declared seeds;
   - the required result format and criteria;
   - a verification procedure;
   - any environmental constraints (TBD: temperature, numeric precision, etc.).
3. **Not** prescribe algorithm, hardware, or compute paradigm.
4. Declare whether workloads are open (public inputs) or “challenge” style (inputs revealed at measurement time) — policy TBD for v0.1+.
5. Be identified by a **version** (e.g. `basket-0.1.0`).

### Basket v0.1 — contents

Concrete locked basket: [`basket-0.1.0/BASKET.md`](./basket-0.1.0/BASKET.md) (BI-W1, BI-W2, BI-W3).

Official index series still requires standardized energy boundaries; see lab procedure.

## 5. Measurement protocol

### 5.1 Principle

The primary observation is the **amount of energy** required to produce the basket results **correctly**, within the declared measurement boundaries.

The following are **not** primary metrics of this specification by themselves:

- operation counts;
- processor type;
- wall-clock time alone (may be reported as metadata).

### 5.2 Steps of a valid run

1. Declare the **version** of basket and protocol.
2. Declare the **system under test** (free-form description: hardware, software, relevant configuration).
3. Execute the workloads **without** violating basket constraints.
4. Apply **verification** to every required workload.
5. Record **energy** within the declared measurement boundary.
6. Publish the logs required for reproduction or audit (format TBD).

A run is **invalid** if verification fails on a required workload, energy boundaries are undeclared, or required logs for that protocol version are missing.

### 5.3 Energy accounting (structure; details TBD)

For every valid run, declare at least:

- energy unit (recommended: joule / watt-hour — **TBD confirmation**);
- boundaries (e.g. CPU/GPU package only, whole machine, rack — **TBD**);
- instrument or method (powermeter, RAPL, PDU, modeled estimate — **TBD**; modeled estimates must be labeled as such);
- time interval aligned with basket execution;
- any corrections (idle subtraction, etc. — **TBD policy**).

### 5.4 Index aggregation (draft)

**TBD.** Possible directions (non-normative in v0.1):

- total basket energy over time;
- weighted average across workloads;
- an index normalized to a declared baseline (e.g. first public observation = 100).

The official formula will be fixed once at least one concrete basket and a reproducible baseline exist.

## 6. Versioning and forks

### 6.1 Versioning

This specification uses document-level semantic versions (`v0.1`, `v0.2`, …).

- Changes that alter the meaning of historical observations require a **new major** basket/protocol version and, in effect, a new series.
- Clarifications with no series impact may be patches/documentation.

### 6.2 Forks

Anyone may publish a derived specification (new basket, new criteria, different scope).

Rules:

1. A fork **must** declare its parent specification and the differences.
2. A fork is a **new** index with a **new** historical series.
3. A fork **must not** rewrite the original index series retroactively.
4. Legitimacy comes from transparency, reproducibility, and adoption — not from a central authority.

## 7. Reproducibility

As far as practical, every published observation should let third parties:

- understand what was executed;
- repeat or audit verification;
- assess the energy boundaries.

Log formats, artifact hashing, and audit checklists: **TBD**.

## 8. Governance / adoption (lightweight)

There is no authority that declares “this is *the* computational efficiency.”

- Adoption of a specification or basket is voluntary.
- Coordination may happen via issues/PRs on public repositories.
- Definition conflicts are preferably resolved with clear **forks** rather than silent rewrites of history.

## 9. Relationship to any future asset

The index and any future financial/crypto asset are **distinct objects**.

This specification:

- does **not** create a token;
- does **not** imply that a token exists or must exist;
- does **not** guarantee that an asset will track the index.

Any economic exposure mechanism is a **separate project phase** and will need its own document.

## 10. Changelog

### v0.1 — 2026-09-24

- First public structural draft: definitions, basket requirements, protocol (with TBD), versioning/forks, reproducibility, lightweight governance.
- No concrete basket; no normative index formula; no asset.
- Spec language: English only.

### v0.1.1 notes — 2026-09-24

- Basket 0.1.0 locked with three workloads + Fedora lab procedure draft.
- Still no official live series; still no token.

## 11. Open questions / future work

1. Which workloads enter the first public basket?
2. Which energy boundaries are rigorous enough and practical enough?
3. How to handle challenge inputs vs open inputs?
4. How to normalize observations across different labs?
5. Which index formula to adopt after a baseline?
6. Whether and how (later phase) an asset could provide exposure to the index without conflating the two objects.

---

End of specification v0.1.
