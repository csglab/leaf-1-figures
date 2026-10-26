#!/usr/bin/env python3
"""Recompute DATA_MANIFEST.tsv and FIGURE_OUTPUTS.tsv from what is on disk.

Run after re-staging data or re-running a notebook, so the checksums match the
committed files. NOTEBOOK_PROVENANCE.tsv is hand-maintained -- it records why a
figure exists, which nothing here can infer.

Usage:
    python figure/make_manifests.py
"""
from __future__ import annotations

import hashlib
from pathlib import Path

FIG = Path(__file__).resolve().parent
MODALITIES = ("cfdna", "scatac", "tcga")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_manifest(subdir: str, dst: Path) -> None:
    rows = []
    for mod in MODALITIES:
        d = FIG / mod / subdir
        if not d.is_dir():
            continue
        for p in sorted(d.rglob("*")):
            if p.is_file():
                rows.append((p.relative_to(FIG).as_posix(), p.stat().st_size, sha256(p)))
    with dst.open("w") as fh:
        fh.write("path\tbytes\tsha256\n")
        for path, size, digest in rows:
            fh.write(f"{path}\t{size}\t{digest}\n")
    total = sum(r[1] for r in rows)
    print(f"{dst.name}: {len(rows)} files, {total / 1e6:.1f} MB")


def main() -> int:
    write_manifest("data", FIG / "DATA_MANIFEST.tsv")
    write_manifest("output", FIG / "FIGURE_OUTPUTS.tsv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
