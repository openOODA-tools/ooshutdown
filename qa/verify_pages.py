#!/usr/bin/env python3
import sys
import os

violations = 0
for root, dirs, files in os.walk("."):
    if "/.git" in root or "/packaging" in root:
        continue
    oo_files = [f for f in files if f.endswith(".oo")]
    if len(oo_files) > 8:
        print(f"ERROR: Directory density violation: {root} has {len(oo_files)} files (max 8)")
        violations += 1
    for f in oo_files:
        path = os.path.join(root, f)
        if f in ["util.oo", "utils.oo", "helper.oo", "helpers.oo", "common.oo", "misc.oo", "shared.oo", "base.oo", "core.oo"]:
            print(f"ERROR: Banned filename: {path}")
            violations += 1
        with open(path) as stream:
            lines = stream.readlines()
        n = len(lines)
        is_shim = all(l.strip().startswith("//") or l.strip().startswith("import ") or l.strip() == "" for l in lines)
        if not is_shim and n < 16:
            print(f"ERROR: Line floor violation: {path} has {n} lines (min 16)")
            violations += 1
        if n > 256:
            print(f"ERROR: Line ceiling violation: {path} has {n} lines (max 256)")
            violations += 1

if violations > 0:
    print(f"FAILED: {violations} Page Rule violation(s) detected.")
    sys.exit(1)

print("PASSED: 100% Page Rule and Directory Density compliance.")
