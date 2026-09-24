# Buy Inefficiency — Pitch

## In one line

We measure how much **less energy** it takes, over time, to do the **same** computational work — and only later, if at all, design a way to take economic exposure to that improvement.

## The problem we see

Computing progress is often told as *more power*: more FLOPS, more parameters, more cloud. There is another story that matters just as much: **doing the same things while consuming less**.

Better algorithms, more efficient chips, less memory traffic, smarter compilers, new compute paradigms. The point is not which brand wins. The point is: *how much useful work do I get per joule?*

What is missing today is a public, comparable, versioned reference that measures exactly that — independent of the technology used.

## What we propose

1. A **public basket** of computational workloads, with clear inputs, expected outputs, and verification rules.
2. A **measurement protocol** that records the energy required to complete that basket correctly.
3. A **versioned index** that tracks how that energy cost evolves over time.
4. **Free forks**: if you disagree with the basket, publish another. You do not erase the original’s history.

We do not prescribe *how* to solve the tasks. An analog system, an ASIC, a cluster, a new algorithm: if it produces the verifiable result with less energy, the index sees it.

## Why the name

Today’s inefficiency is the room still left for progress to compress consumption. “Buying inefficiency” means, in prospect, taking exposure to improvement in that resources-to-work ratio.

**Important:** index and token are not the same thing. First we define and publish what we measure. Only in a **separate** later phase might we design an asset for economic exposure to the index. That phase has not started.

## What exists now (free)

- Draft **Index Spec v0.1**
- This pitch
- A public repository open to issues, workload proposals, and forks

No token for sale. No invented index numbers. No “live index” until the basket and protocol are concrete and reproducible.

## What comes next

- Choose the first workloads for basket v0.1
- Make energy measurement boundaries operational (lab / procedures)
- Publish the first reproducible time series
- Only then: discuss exposure mechanisms (if they make sense)

## Why share this now

Good measures are born in public. Transparency, reproducibility, and adoption matter more than a central authority declaring “this is *the* efficiency.”

If the idea resonates: read the spec, open an issue, propose a workload, or fork the basket.

See the project README for links.
