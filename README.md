# LEAF-1 figure reproducibility

Code and processed data to regenerate the figures in the LEAF-1 manuscript.
Each notebook reads tables staged in the repository and writes figure files.
Model checkpoints, H5 files, and raw sequencing data are not required.

## Organization

```
leaf-1-figures/
├── cfdna/
│   ├── notebook/   one notebook per figure (see map below)
│   ├── data/       input tables read by the notebooks
│   └── output/     generated figures (.png, .pdf) and derived tables
├── scatac/
│   ├── notebook/   one notebook per figure (see map below)
│   ├── data/       input tables read by the notebooks
│   └── output/     generated figures (.png, .pdf) and derived tables
├── other/
│   ├── notebook/   model-overview pretraining curves
│   ├── data/       input tables read by the notebook
│   ├── diagrams/   schematic source files
│   └── output/     generated figures and derived tables
├── src/leaf1figures/        shared matplotlib style (set_paper_style, savefig, OKABE_ITO)
├── NOTEBOOK_PROVENANCE.tsv  notebook, figure, source analysis notebook, input tables
├── DATA_MANIFEST.tsv        size and SHA-256 for each input table
├── FIGURE_OUTPUTS.tsv       size and SHA-256 for each output
├── environment.yml
├── CITATION.cff
├── LICENSE
└── LICENSE-DATA
```

Notebooks, input tables, and outputs are grouped by modality (`cfdna`, `scatac`).
Each notebook reads only from the `data/` directory next to it and writes only to
the adjacent `output/` directory. Notebooks are committed with their cell outputs.

## Figure map

scATAC (`scatac/notebook/`):

| Notebook | Manuscript figure |
|---|---|
| `scatac_celltype_classification.ipynb` | Figure 2b-f |
| `scatac_tf_motif_accessibility.ipynb` | Figure 3a-d |
| `scatac_fragment_umap.ipynb` | Figure 3e-f |
| `supp_scatac_classification_extended.ipynb` | Supplementary Figures 1-3 |
| `supp_scatac_embedding_vs_binning_resolution.ipynb` | Supplementary Figure 4 |
| `supp_scatac_segment_ablation.ipynb` | Supplementary Figure 5 |

cfDNA (`cfdna/notebook/`):

| Notebook | Manuscript figure |
|---|---|
| `cfdna_representation_benchmark.ipynb` | Figure 4b-e |
| `cfdna_mil_detection.ipynb` | Figure 5b-e |
| `cfdna_ctdna_detection.ipynb` | Figure 5f-g |
| `cfdna_ichorcna_genomewide.ipynb` | Figure 6b |
| `kidney_zeroshot.ipynb` | Figure 6c-d |
| `kidney_zeroshot_leaf1_vs_binning_auc.ipynb` | Figure 6e |
| `supp_cfdna_per_cancer_metrics.ipynb` | Supplementary Figure 8 |
| `supp_cfdna_subsampling.ipynb` | Supplementary Figures 7, 9-13 |

Model overview (`other/notebook/`):

| Notebook | Manuscript figure |
|---|---|
| `pretraining_curves.ipynb` | Pretraining curves (model overview) |

## Setup

```bash
conda env create -f environment.yml
conda activate leaf1-paper-repro
```

## Running

Open a notebook in Jupyter and run it top to bottom. The first cell resolves the
`data/`, `output/`, and `src/` paths, so a notebook runs from its own directory,
from its modality directory, or from the repository root.

To regenerate all figures without opening Jupyter:

```bash
jupyter nbconvert --to notebook --execute --inplace */notebook/*.ipynb
```

PNG and table outputs are deterministic under fixed random seeds. PDF outputs
are visually identical across runs but not byte-identical, because matplotlib
records a creation timestamp in PDF metadata. The checksums in
`FIGURE_OUTPUTS.tsv` correspond to the committed files.

## Updating a figure

1. Identify the notebook from the figure map.
2. To change styling or layout, edit the notebook. To change the underlying
   numbers, replace or add a table in the modality `data/` directory and update
   the notebook to read it.
3. Re-run the notebook so `output/` and the embedded cell outputs refresh.
4. If `data/` or `output/` files changed, update `DATA_MANIFEST.tsv` and
   `FIGURE_OUTPUTS.tsv` accordingly.

## License

- Code (notebooks and `src/leaf1figures/`): MIT, see `LICENSE`.
- Data and figures (`*/data/`, `*/output/`): CC-BY-4.0, see `LICENSE-DATA`.
- Some bundled data are third party and retain their original licenses (see below).

Please cite the LEAF-1 paper (`CITATION.cff`).

## Data sources

- Transcription-factor motifs (scATAC motif figure): JASPAR database (CC0).
- scATAC-seq metadata and atlas-derived tables: human single-cell
  chromatin-accessibility atlas of Zhang et al., 2021, Cell 184(24):5985-6001.e19,
  doi:10.1016/j.cell.2021.10.024, source data at http://catlas.org/. Sample
  identifiers are public consortium codes.
- cfDNA tables: model outputs for the cell-free DNA cohort of Cristiano et al.,
  2019, Nature 570:385-389. The underlying fragmentation profiles are available
  through FinaleDB (Zheng et al., 2021, Bioinformatics 37:2502-2503,
  doi:10.1093/bioinformatics/btaa999; http://finaledb.research.cchmc.org/), a
  public database of cell-free DNA
  fragmentation patterns. Please cite Cristiano et al.
  (2019) and FinaleDB if you reuse these.
- Kidney prediction tables: model outputs for an independently profiled,
  de-identified clinical cohort (pseudonymous codes only; no names, dates, or
  other identifiers).
