# Buy Inefficiency

Buy Inefficiency is a public, versioned specification for an index of **computational efficiency**: how much energy is required, over time, to correctly complete a fixed basket of computational workloads. The method of computation is not prescribed.

An optional later phase may design an asset for economic exposure to that index. **The index and any token are distinct objects.**

## What it is

Progress in computing is not only more power. It is also the ability to get the **same results with fewer physical resources** — especially less energy — without depending on a specific technology, company, or architecture.

The system uses a **public basket of computational workloads**. For each job we define inputs, the required result, and verification conditions. We do **not** prescribe how the result must be obtained. What matters is the energy needed to produce correct results.

When new techniques (hardware, algorithms, memory systems, compilers, compute paradigms, or innovations we cannot foresee today) reduce the energy needed for the same basket, the index records an efficiency increase. The index **does not pick a technology winner**; it measures the outcome of progress, whatever its origin.

## What it is not (yet)

- **Not a token.** Defining the index says *what* is measured. It does not, by itself, make an asset track that value economically.
- **Not a universal, final measure** of computational efficiency. It is a public, versioned specification. A community may adopt it or publish a derived fork. Each fork is a **new** index and does not rewrite the original historical series.
- **Not a ranking of companies or chips.** It does not crown a vendor; it tracks energy outcomes on the basket.

## Project status

| Piece | Status |
|-------|--------|
| Idea and economic principle | Documented |
| [Index Spec v0.1](./INDEX_SPEC_v0.1.md) | Public draft |
| [Pitch](./PITCH.md) | Public draft |
| Concrete workload basket | TBD |
| Lab / energy measurement details | Structured; details TBD |
| Asset / exposure token | **Not started** (separate phase) |

## Economic principle

*Buy Inefficiency* means seeking exposure to the gap between what computing can do today and what it will be able to do in the future with the **same** physical resources.

The underlying hypothesis is not about a particular company, cryptocurrency, or technology. It is about the general ability to keep improving the ratio of resources consumed to computational work produced.

## Documents

- [`INDEX_SPEC_v0.1.md`](./INDEX_SPEC_v0.1.md) — formal index specification
- [`PITCH.md`](./PITCH.md) — short shareable pitch
- [`CONTRIBUTING.md`](./CONTRIBUTING.md) — how to propose workloads, forks, and issues

## License

Contents of this repository: [CC BY 4.0](./LICENSE).

## Author

Gio Mario Lasagna — initial draft, September 2026.
