from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


OKABE_ITO = {
    "blue": "#0072B2",
    "orange": "#D55E00",
    "green": "#009E73",
    "yellow": "#F0E442",
    "sky": "#56B4E9",
    "vermillion": "#D55E00",
    "purple": "#CC79A7",
    "black": "#000000",
    "gray": "#777777",
}


def set_paper_style():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "DejaVu Sans", "Helvetica", "Liberation Sans"],
        "font.size": 7,
        "axes.titlesize": 8,
        "axes.labelsize": 7,
        "xtick.labelsize": 6,
        "ytick.labelsize": 6,
        "legend.fontsize": 6,
        "axes.linewidth": 0.5,
        "xtick.major.width": 0.5,
        "ytick.major.width": 0.5,
        "figure.dpi": 150,
        "savefig.dpi": 600,
        "savefig.bbox": "tight",
        # Embed fonts as editable text (TrueType / Type 42) rather than Type 3,
        # and keep SVG text as <text> instead of converting glyphs to <path>,
        # so Illustrator recognizes labels as editable text.
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def savefig(fig, outdir, stem, data=None, index=False):
    """Save ``fig`` as PDF, PNG and SVG under ``outdir`` with the given ``stem``.

    If ``data`` is provided, also write the exact values behind the plot as a
    tidy TSV at ``outdir/stem.tsv``. ``data`` may be a pandas DataFrame/Series
    or anything ``pandas.DataFrame`` accepts (e.g. a dict of equal-length
    columns). Pass ``index=True`` to keep the DataFrame index as the first
    column (use this when the row labels carry meaning, e.g. a matrix).
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    fig.savefig(outdir / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(outdir / f"{stem}.png", dpi=600, bbox_inches="tight")
    fig.savefig(outdir / f"{stem}.svg", bbox_inches="tight")
    print(f"saved: {outdir / (stem + '.pdf')}")
    print(f"saved: {outdir / (stem + '.png')}")
    print(f"saved: {outdir / (stem + '.svg')}")
    if data is not None:
        df = data.to_frame() if isinstance(data, pd.Series) else (
            data if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
        )
        df.to_csv(outdir / f"{stem}.tsv", sep="\t", index=index)
        print(f"saved: {outdir / (stem + '.tsv')}")
