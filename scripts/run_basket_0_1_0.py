#!/usr/bin/env python3
"""Run Buy Inefficiency basket 0.1.0 and optionally wrap with RAPL energy_uj.

Unofficial helper. Does not claim an official index point.
"""
from __future__ import annotations

import hashlib
import json
import struct
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASKET = ROOT / "basket-0.1.0"


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def run_w1() -> None:
    raw = (BASKET / "w1-canonical-lines/input.txt").read_text(encoding="utf-8")
    lines = []
    for line in raw.splitlines():
        if line.endswith("\r"):
            line = line[:-1]
        lines.append(line)
    canon = "\n".join(sorted(set(lines), key=lambda s: s.encode("utf-8"))) + "\n"
    got = sha256_bytes(canon.encode("utf-8"))
    exp = (BASKET / "w1-canonical-lines/expected_sha256.txt").read_text().strip()
    if got != exp:
        raise SystemExit(f"W1 FAIL sha {got} != {exp}")
    print("W1 OK", got)


def run_w2() -> None:
    meta = json.loads((BASKET / "w2-matmul/meta.json").read_text())
    n = meta["n"]

    def load(path: Path):
        raw = path.read_bytes()
        vals = list(struct.unpack("<" + "d" * (n * n), raw))
        return [vals[i * n : (i + 1) * n] for i in range(n)]

    A = load(BASKET / "w2-matmul/A.bin")
    B = load(BASKET / "w2-matmul/B.bin")
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            aik = A[i][k]
            for j in range(n):
                C[i][j] += aik * B[k][j]
    out = bytearray()
    for row in C:
        for x in row:
            out += struct.pack("<d", float(x))
    got = sha256_bytes(bytes(out))
    exp = meta["sha256"]["C_expected"]
    if got != exp:
        raise SystemExit(f"W2 FAIL sha {got} != {exp}")
    print("W2 OK", got)


def run_w3() -> None:
    model = "1 -2 3 4 -5 6 7 -8\n"
    p = subprocess.run(
        [sys.executable, str(BASKET / "w3-sat/verify_model.py")],
        input=model,
        text=True,
        capture_output=True,
    )
    if p.returncode != 0:
        raise SystemExit(f"W3 FAIL: {p.stderr}")
    print("W3 OK", model.strip())


def read_rapl_uj() -> int | None:
    path = Path("/sys/class/powercap/intel-rapl:0/energy_uj")
    if not path.exists():
        return None
    return int(path.read_text().strip())


def main() -> None:
    start_uj = read_rapl_uj()
    t0 = time.perf_counter()
    run_w1()
    run_w2()
    run_w3()
    elapsed = time.perf_counter() - t0
    end_uj = read_rapl_uj()

    energy = None
    method = "none"
    modeled = True
    boundary = "unavailable"
    if start_uj is not None and end_uj is not None:
        if end_uj >= start_uj:
            energy = (end_uj - start_uj) / 1_000_000.0
            method = "intel-rapl:0/energy_uj"
            modeled = False
            boundary = "pkg-rapl"
        else:
            print("RAPL counter wrapped; discard energy", file=sys.stderr)

    run = {
        "spec_version": "0.1",
        "basket_version": "basket-0.1.0",
        "protocol_version": "protocol-0.1-draft",
        "system_under_test": {
            "description": "auto run via scripts/run_basket_0_1_0.py",
            "hardware": "see notes",
            "software": f"python {sys.version.split()[0]}",
        },
        "energy": {
            "amount": energy if energy is not None else 0,
            "unit": "J",
            "boundary": boundary,
            "method": method,
            "modeled_estimate": modeled if energy is not None else True,
        },
        "verification": {"passed": True, "details": "W1 W2 W3 OK"},
        "wall_time_seconds": round(elapsed, 6),
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "official": False,
        "notes": "Unofficial. Fill hardware description before publishing.",
    }
    if energy is None:
        run["notes"] += " No RAPL energy available on this host."
        run["verification"]["details"] += "; energy not measured"

    out = Path("measurement-run.json")
    out.write_text(json.dumps(run, indent=2) + "\n")
    print(json.dumps(run, indent=2))
    print("wrote", out.resolve())


if __name__ == "__main__":
    main()
