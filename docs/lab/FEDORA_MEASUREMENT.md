# Fedora lab measurement procedure (draft)

**Goal:** Measure energy to correctly finish basket `0.1.0` on a Fedora workstation, with enough detail for someone else to critique the boundary.

**Status:** Draft procedure — runs are **not** official index points until boundaries and tooling are standardized.

## 0. Safety and honesty

- Label every run `official: false` until the project says otherwise.
- If you use modeled estimates (RAPL gaps, sampling), set `energy.modeled_estimate: true`.
- Do not publish a “Buy Inefficiency price” or token claim from these runs.

## 1. Machine prep (Fedora)

1. Note kernel, CPU, GPU, and power tooling:
   ```bash
   uname -r
   lscpu | head
   # RAPL present?
   ls /sys/class/powercap/intel-rapl 2>/dev/null || echo "no intel-rapl"
   ```
2. Prefer a quiet system: close browsers/GPU training jobs; note what you could not stop.
3. Fix CPU governor if you document it (example only — choose deliberately):
   ```bash
   cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
   ```
4. Record ambient notes (optional): room temp, AC power vs battery (desktop should be AC).

## 2. Declare the energy boundary

Pick **one** and stick to it for the run:

| Boundary ID | Meaning | Typical tool |
|-------------|---------|--------------|
| `pkg-rapl` | CPU package RAPL energy | `intel-rapl` / `perf` / `powercap` |
| `psys-rapl` | Platform RAPL if available | `intel-rapl:psys` |
| `wall-pdu` | Wall energy at PDU/kill-a-watt | External meter |
| `whole-machine-est` | Estimated whole box | Document model; mark modeled |

**Recommendation for first Fedora runs:** `pkg-rapl` if available; otherwise `wall-pdu`.

## 3. Obtain the basket

```bash
git clone https://github.com/giomariolasagna-ux/buy-inefficiency.git
cd buy-inefficiency
# artifacts under basket-0.1.0/
```

## 4. Example RAPL wrap (illustrative)

This is a template, not the only valid method:

```bash
# Read package energy_uj before/after (intel RAPL)
read_uj() { cat /sys/class/powercap/intel-rapl:0/energy_uj; }

START=$(read_uj)
# --- run all three workloads with YOUR solver/pipeline ---
# W1, W2, W3 must verify before you accept the energy number
END=$(read_uj)
echo "energy_J=$(( (END-START)/1000000 ))"
```

If `energy_uj` counter wraps, discard the run.

## 5. Verification checklist

- [ ] W1 SHA-256 matches `expected_sha256.txt`
- [ ] W2 SHA-256 matches `C_expected`
- [ ] W3 `verify_model.py` returns OK
- [ ] Energy boundary ID recorded
- [ ] Tool/method recorded
- [ ] Wall time optional metadata recorded

## 6. Publish a run object

Fill `schemas/measurement-run.schema.json` (see `schemas/example-run.invalid-demo.json` for shape). Keep `"official": false`.

Open a GitHub issue titled `[run] fedora <date>` and paste the JSON, or attach the file.

## 7. What Fedora is good for here

- Iterating solvers and pipelines for W1–W3
- Comparing RAPL vs PDU on the same box
- Stressing reproducibility docs

Fedora **cannot** pay Ethereum gas. It **can** make the index real through measurements.
