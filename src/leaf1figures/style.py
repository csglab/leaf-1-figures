from pathlib import Path

import matplotlib.pyplot as plt


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
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def savefig(fig, outdir, stem):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    fig.savefig(outdir / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(outdir / f"{stem}.png", dpi=600, bbox_inches="tight")
    print(f"saved: {outdir / (stem + '.pdf')}")
    print(f"saved: {outdir / (stem + '.png')}")
