# Buy Inefficiency

Buy Inefficiency is a public, versioned specification for an index of **computational efficiency**: how much energy is required, over time, to correctly complete a fixed basket of computational workloads. The method of computation is not prescribed.

An optional later phase may design an asset for economic exposure to that index. **The index and any token are distinct objects.**

<p align="center">
  <img src="assets/mark.png" alt="Buy Inefficiency mark" width="120" />
</p>

**Site:** https://giomariolasagna-ux.github.io/buy-inefficiency/

## What it is

Progress in computing is not only more power. It is also the ability to get the **same results with fewer physical resources** — especially less energy — without depending on a specific technology, company, or architecture.

The system uses a **public basket of computational workloads**. For each job we define inputs, the required result, and verification conditions. We do **not** prescribe how the result must be obtained. What matters is the energy needed to produce correct results.

When new techniques reduce the energy needed for the same basket, the index records an efficiency increase. The index **does not pick a technology winner**.

## What it is not (yet)

- **Not a token.** Defining the index says *what* is measured. It does not make an asset track that value.
- **Not a universal final measure.** Specs can be forked; each fork is a new index.
- **Not a vendor ranking.**

## Project status

| Piece | Status |
|-------|--------|
| Idea and economic principle | Documented |
| [Index Spec v0.1](./INDEX_SPEC_v0.1.md) | Public draft |
| [Pitch](./PITCH.md) | Public draft |
| [Basket proposals](./BASKET_PROPOSALS.md) | Candidates only |
| [Measurement run schema](./schemas/measurement-run.schema.json) | Draft |
| [Site](https://giomariolasagna-ux.github.io/buy-inefficiency/) | GitHub Pages |
| Concrete locked basket | TBD |
| Asset / exposure token | **Not started** |

## Documents

- [`INDEX_SPEC_v0.1.md`](./INDEX_SPEC_v0.1.md) — formal index specification
- [`PITCH.md`](./PITCH.md) — short shareable pitch
- [`BASKET_PROPOSALS.md`](./BASKET_PROPOSALS.md) — candidate workloads (not locked)
- [`FAQ.md`](./FAQ.md) · [`ROADMAP.md`](./ROADMAP.md) · [`SOCIAL.md`](./SOCIAL.md)
- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`schemas/`](./schemas/) — JSON Schema for measurement runs

## License

Contents of this repository: [CC BY 4.0](./LICENSE).

## Author

Gio Mario Lasagna — initial draft, September 2026.
