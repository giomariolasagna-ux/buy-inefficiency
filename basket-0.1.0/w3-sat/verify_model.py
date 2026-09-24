#!/usr/bin/env python3
"""Verify a DIMACS-like assignment against instance.cnf. Exit 0 if OK."""
import sys
from pathlib import Path

def load_cnf(path):
    clauses = []
    nvars = None
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("c"):
            continue
        if line.startswith("p"):
            parts = line.split()
            nvars = int(parts[2])
            continue
        lits = [int(x) for x in line.split() if x != "0"]
        if lits:
            clauses.append(lits)
    return nvars, clauses

def parse_model(text):
    vals = {}
    for tok in text.replace(",", " ").split():
        if tok in ("v", "sat", "SAT"): continue
        x = int(tok)
        if x == 0: continue
        vals[abs(x)] = x > 0
    return vals

def main():
    cnf = Path(__file__).with_name("instance.cnf")
    nvars, clauses = load_cnf(cnf)
    model_text = sys.stdin.read() if len(sys.argv) < 2 else Path(sys.argv[1]).read_text()
    model = parse_model(model_text)
    for i in range(1, (nvars or 0) + 1):
        if i not in model:
            print(f"missing variable {i}", file=sys.stderr)
            return 1
    for ci, clause in enumerate(clauses, 1):
        if not any((lit > 0) == model[abs(lit)] for lit in clause):
            print(f"clause {ci} unsatisfied: {clause}", file=sys.stderr)
            return 1
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
