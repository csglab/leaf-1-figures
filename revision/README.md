# LEAF-1 revision figures

Notebooks and staged tables that regenerate the figures produced for the
reviewer response. Same layout and conventions as the `leaf-1-figures`
repository, so these can be merged into it once the figures have manuscript
numbers.

Each notebook reads only the tables in the `data/` directory next to it and
writes only to the adjacent `output/`. Nothing here needs the analysis data
(`../data/`, 3.5 GB), the upstream H5 files, or any path outside `figure/`.

## Organization

```
figure/
├── cfdna/
│   ├── notebook/   one notebook per figure group (see map below)
│   ├── data/       input tables read by the notebooks
│   └── output/     generated figures (.pdf, .png, .svg) and source-data .tsv
├── scatac/
│   ├── notebook/
│   ├── data/
│   └── output/
├── tcga/
│   ├── notebook/
│   ├── data/
│   └── output/
├── src/leaf1figures/        shared matplotlib style (set_paper_style, savefig, OKABE_ITO)
├── make_manifests.py        recompute the two checksum manifests
├── NOTEBOOK_PROVENANCE.tsv  notebook, figure, source script + command, input tables, original path, deviation
├── DATA_MANIFEST.tsv        size and SHA-256 for each input table
├── FIGURE_OUTPUTS.tsv       size and SHA-256 for each output
└── environment.yml
```

## Figure map

cfDNA (`cfdna/notebook/`):

| Notebook | Outputs |
|---|---|
| `cfdna_epithelial_contribution.ipynb` | `cfdna_epithelial_marker_percentiles`, `cfdna_epithelial_celltype_ora` |
| `cfdna_mil_vs_lr.ipynb` | `cfdna_mil_vs_lr_delta` |
| `cfdna_taskspecific_benchmark.ipynb` | `cfdna_taskspecific_main` (main-figure panel) |
| `cfdna_hybrid_emb_bin.ipynb` | `cfdna_hybrid_emb_bin_auc` |
| `cfdna_loco_nocristiano.ipynb` | `cfdna_loco_nocristiano_specific_vs_loco` |
| `cfdna_nocristiano_paired.ipynb` | `cfdna_nocristiano_delta_forest` (a), `cfdna_nocristiano_auc_bars` (b): Cristiano-free vs released encoder, 10k fragments (2.M1 Supp. Fig.) |
| `cfdna_nocristiano_fig5.ipynb` | `cfdna_nocristiano_pan_cancer_roc` (Fig. 5b), `cfdna_nocristiano_per_cancer_auc` (Fig. 5c), `cfdna_nocristiano_ctdna_logit_forest` (Fig. 5g): Cristiano-free encoder, 10k fragments (2.M1) |
| `cfdna_pretraining_ablations.ipynb` | `cfdna_pretraining_ablations`: controlled pretraining ablations (no [CUT], equal [CUT] masking, no flank, no modality token), a input schematic, b ΔAUC vs full model (linear SVM + MIL), c single readouts (2.M5 Supp. Fig.) |
| `cfdna_kidney_length_matching.ipynb` | `cfdna_kidney_length_matching_bin_fusions` (Fig. 6e variant) |
| `cfdna_kidney_coordinate_baselines.ipynb` | `cfdna_kidney_coordinate_baselines_depth` (Supp. Fig. X) |
| `cfdna_kidney_length_ablation.ipynb` | `cfdna_kidney_length_ablation_depth` (Supp. Fig. Y) |
| `cfdna_kidney_zeroshot.ipynb` | `cfdna_kidney_zeroshot_auc_extended`: zero-shot AUC on the kidney cohort for 8 sequence representations (mean pool + linear SVM and the identical 10k-bag MIL), coordinate binning at 6 widths and 5 task-specific methods (Fig. 6c-e comment) |
| `cfdna_fragment_subsampling_seeds.ipynb` | `cfdna_fragment_subsampling_seeds` (Fig. 5d), `cfdna_fragment_efficiency_seeds` (Fig. 5e), `cfdna_subsampling_seeds_vs_healthy`, `cfdna_subsampling_seeds_vs_other` (Supp. Figs 12-13), `cfdna_subsampling_variability` (new Supp. Fig.), `cfdna_subsampling_seeds_table` (Supp. Table) |
| `cfdna_dnalm_baselines.ipynb` | `cfdna_kmer_lm_delta_auc`, `cfdna_external_lm_model_size` |
| `cfdna_ctdna_bin_auc.ipynb` | `cfdna_ctdna_bin_auc_breast` |

scATAC (`scatac/notebook/`):

| Notebook | Outputs |
|---|---|
| `scatac_atlas_grouped_cv.ipynb` | `scatac_grouped_cv_auc` (a, Zhang atlas; b, Becker 2023) |
| `scatac_leaf1_vs_snapatac_auc.ipynb` | `scatac_leaf1_vs_snapatac_auc`, `scatac_leaf1_vs_snapatac_auc_ntissues` |
| `scatac_atlas_representation_comparison.ipynb` | `scatac_atlas_umap_panel_by_category_supp`, `scatac_atlas_scib_summary_supp` (1,000 fragments); `scatac_atlas_fulldepth_umap_panel_by_category_supp`, `scatac_atlas_fulldepth_scib_summary_supp` (full depth) |
| `scatac_gse129785_validation.ipynb` | `scatac_gse129785_umap_panel_by_celltype_main`, `scatac_gse129785_scib_summary_main` (main-figure size) |
| `scatac_ccre_fragment_ablation.ipynb` | `scatac_ccre_fragment_ablation` |
| `scatac_hybrid_emb_bin.ipynb` | `scatac_hybrid_emb_bin_auc` |
| `supp_scatac_embedding_vs_binning_resolution.ipynb` | `scatac_embedding_vs_binning_resolution` (Supp. Fig. 4, revised) |
| `scatac_motif_fire_vs_homer.ipynb` | `scatac_motif_fire_vs_homer` |
| `scatac_dnalm_baselines.ipynb` | `scatac_dnalm_delta_auc`: LEAF-1 vs external DNA LMs and k-mer baselines on 1,000 atlas cells, biosample-grouped vs cell-level CV (3.M5 Supp. Fig.; Ali's figure) |

TCGA (`tcga/notebook/`):

| Notebook | Outputs |
|---|---|
| `tcga_layer_sweep.ipynb` | `tcga_layer_sweep_auc` |

Outputs were renamed on the way in: two of the original files were both called
`scib_matched_classifier_probabilities.png` and would have collided in a flat
`output/`. `NOTEBOOK_PROVENANCE.tsv` records each figure's original path under
`../output/`.

## Running

```bash
conda env create -f environment.yml
conda activate leaf1-paper-repro
```

Open a notebook and run it top to bottom. The first cell resolves `data/`,
`output/` and `src/` itself, so a notebook runs from its own directory or from
its modality directory. To regenerate everything:

```bash
cd figure && jupyter nbconvert --to notebook --execute --inplace */notebook/*.ipynb
```

## Where the numbers come from

Each staged table is the **cut point** for its figure: the smallest table that
still holds every number the panel draws. Everything upstream of it -- UMAP
fitting, the scIB panel, SnapATAC, grouped CV, the MIL/LR sweeps, the
contribution and ORA analyses -- stays in `../src/` and is *not* re-run here.
Most of it needs cluster storage that is not mounted everywhere, which is
exactly why the cut point exists.

`../stage_data.py` (in the analysis directory, not in this repo) is the
bridge. It reads `../output/`, `../data/` and the upstream cell metadata, and
writes `*/data/`. Running it is not required to reproduce the figures; it
exists so every staged table has a recorded origin and so a re-run of an
upstream analysis can be pushed through in one command.

Two details there are load-bearing rather than cosmetic:

* Staged floats are written at `%.17g` and read back with
  `float_precision="round_trip"`. pandas' defaults lose the last significant
  digit on both sides, which is enough to move an autoscaled axis limit onto a
  different tick and shift a whole panel by a pixel.
* UMAP coordinates are copied at full precision. Rounding them to 4 decimals
  moves about 0.1% of the rendered pixels.

## Reproduction status

Of the twenty-seven figures that redraw an existing file under `../output/`, fourteen come
out **byte-identical** to it. The thirteen that do not are listed in the `deviation`
column of `NOTEBOOK_PROVENANCE.tsv`:

* `cfdna_loco_nocristiano_specific_vs_loco` -- redrawn in this directory's style
  from `../output/cfdna/cfdna_loco_noCristiano/cancer_specific_vs_loco_noCristiano.png`:
  title, subtitle and footnotes moved to the legend; Okabe-Ito blue/orange
  markers; same values.

* `scatac_atlas_*_supp` and `scatac_atlas_fulldepth_*_supp` -- the atlas UMAP
  and scIB panels at 1,000 fragments and at full depth, redrawn at 180 mm from
  `../output/scatac/umap_comp/summary/{panel_allbins_classifier_probabilities,
  scib_matched_classifier_probabilities}{,_fulldepth}*.png`: UMAPs as two rows of
  four with the legend in the eighth slot, wrapped titles; scIB rows named and
  coloured LEAF-1 (were "classifier probs"), coordinate bins grey, legend above,
  cross-donor kNN purity dropped. Same coordinates, metric values and row order.
  The response-size versions are no longer kept here.

* `cfdna_kidney_length_ablation_depth` -- Supp. Fig. Y, redrawn because its plot
  script is on the rrg-hsn cluster. Its values are the LEAF-1, DELFI and
  fragment-length rows of the table Fig. 6e reads, identical to the source
  plot's own table. Same colours and line styles; "LEAF1" spelt LEAF-1; title
  and subtitle moved to the legend; panel letters a-c; 180 mm wide (was 189 mm).

* `cfdna_kidney_coordinate_baselines_depth` -- Supp. Fig. X, redrawn from the
  bootstrap run's `condition_metrics.csv` (per-bag AUCs, the lines) and
  `depth_summary.csv` (bootstrap CI, the bands), because the source plot script
  takes its colours and markers from `09_plot_subsampling_v2.py`, which is on
  the rrg-hsn cluster and not here. LEAF-1 takes its blue (was a
  black dashed line); fragment length moves to near-black (it shared the sky
  blue of the ~100 kb bins); title, subtitle and footnote move to the legend;
  panel letters a-d; 179 mm wide (was 184 mm). Same values and bands.

* `scatac_hybrid_emb_bin_auc` -- redrawn from
  `../output/scatac/scatac_hybrid_emb_bin/hybrid_scatac_scatter_supp.png` in
  the published Supplementary Figure 4's code and size (5.2 in square, 5-6 pt
  text, per-panel limits of data range +/- 0.02). Points take Okabe-Ito blue and
  vermillion (originally another blue and orange). Same 102 cell types, values,
  panel order and bin-size labels.

* `scatac_embedding_vs_binning_resolution` -- Supp. Fig. 4, revised. The
  published notebook (leaf-1-figures, same name) plotted the pooled
  out-of-fold LEAF-1 AUC (`scatac_task_metrics.csv` `auc`, via
  `scatac_leaf1_vs_binning_auc.csv`) against the mean of the five per-fold
  binning AUCs. Both axes are now the per-fold mean from
  `scatac_coordinate_binning_auc_by_fold.csv`, the table and reduction of the
  main-figure panel `scatac_leaf1_vs_coordinate_binning`, so panel c matches it
  point for point. LEAF-1 mean AUC 0.930 -> 0.935; embedding higher in 61, 92,
  102, 102 of 102 cell types at 300, 100, 30, 10 kb (was 58, 87, 101, 102).
  Per-panel limits (data range +/- 0.02) as published; tick labels now two
  decimals on every panel (panel d had one). At merge,
  `scatac_leaf1_vs_binning_auc.csv` has no other reader and can be dropped.

* `cfdna_hybrid_emb_bin_auc` -- redrawn for the supplement from
  `../output/cfdna/cfdna_hybrid_emb_bin/hybrid_auc_bars_all_bins.png` at 180 mm
  width. Rows are labelled by bin size (300kb, 100kb, 30kb, 10kb), not by bin
  count: the original's "10k genomic bins" is 10,000 bins of ~310 kb, the
  coarsest row. LEAF-1 is in LEAF-1 blue and the bins in Fig. 4's comparator
  grey (originally another blue and orange); the title and subtitle move to the
  legend. Same values, CIs and row order.

* `scatac_ccre_fragment_ablation` -- restyled for the supplement from
  `../output/scatac/scatac_ccre_fragment_ablation/plot_ccre_ablation.py`: no AUC
  tick above 1.0, the P value typeset as
  2.7 × 10^-15, and each cell type's connecting line now meets its own jittered
  points (the original drew the lines at the box centres). Same 102 cell types,
  values, colours and paired t-test.

* `scatac_leaf1_vs_snapatac_auc` and `scatac_leaf1_vs_snapatac_auc_ntissues`
  -- re-scored on 2026-11-03 with the Figure 2e classifier (L2 logistic
  regression, lbfgs, `class_weight="balanced"`, C by inner stratified 3-fold CV
  over 0.001-100) and the Figure 2e metric (per task, the mean of the five
  outer-fold AUCs). The LEAF-1 values are the saved Figure 2e predictions
  (mean 0.935458); SnapATAC 5 kb + MNC was refitted on the 10,130 cells its QC
  kept (mean 0.953241, higher in 74/102 tasks). The originals in
  `../output/scatac/auc_leaf1_vs_snapatac*.png` used a fixed C = 0.316, no
  class weights and pooled out-of-fold AUC (0.9253 vs 0.9490), so their points
  differ. Run: `../runs/scatac_fig2e_classifier_20261103/`; tables:
  `../output/scatac/fig2e_classifier_leaf1_vs_snapatac/`. Also restyled for the
  supplement: LEAF-1 takes the blue it has in every other figure (the
  originals drew it orange), the four cell-type annotations are dropped, and
  the dot-size key sits below the upper-left points rather than over them.
* `tcga_layer_sweep_auc` -- its original is not under `../output/` but in the
  upstream project (`pool/notebook_tcga/fig_tcga_layer_sweep_auc.png`). Every
  plotted value is identical to the upstream `tcga_layer_sweep.csv`; about 0.7%
  of PNG pixels differ in anti-aliasing because the upstream panel was rendered
  with matplotlib 3.8.0 and this environment has 3.10.8.

Eleven more figures are new here and have no original to compare against:

* The four `cfdna_*_seeds*` panels (Fig. 5d-e, Supp. Figs 12-13) for Comment
  2.m3: the published panels (leaf-1-figures `cfdna_mil_detection.ipynb`,
  `supp_cfdna_subsampling.ipynb`) with the same code and layout, drawn from 40
  fragment subsamples per depth (4 seeds) instead of seed 42's 10. Bands are the
  BCa CI over 200 fold x subsample AUCs (published: 50); "Embedding" is named
  LEAF-1. The published values are exactly seed 42 of the new table.
* `cfdna_subsampling_variability`, a new supplementary figure from the same table:
  spread across the 40 subsamples (a, pan-cancer AUC; b, paired gain over Bin +
  Length), on Fig. 5d's linear axis extended down to 100 fragments. The Fig. 5e
  gains with bootstrap 95 % CIs are a table, `cfdna_fragment_efficiency_seeds_ci.tsv`.
* `scatac_motif_fire_vs_homer`. It replaces the two cell-type-background
  scatters `../output/scatac/motif_analysis/motif_comparison_out/figures/
  fire_vs_homer_{Club_Cell,Atrial_Cardiomyocyte}_scatter_celltype_only.png` with
  one two-panel figure from the same per-motif table: LEAF-1/FIRE-only points in
  LEAF-1 blue (were red), the two empty legend classes dropped, Spearman rho of
  the plotted axes added. The script that drew the originals is not on this
  server.
* `cfdna_ctdna_bin_auc_breast`.
* `cfdna_taskspecific_main`. LEAF-1 and the three task-specific methods from
  `../output/cfdna/taskspecific/cfdna_taskspecific_benchmark.png`, drawn with
  Fig. 4c's code; y axis from 0.4 because one EMIT task sits at 0.458. The
  seven-bar response version is no longer kept here.
* The two GSE129785 panels (`scatac_gse129785_*_main`). They redraw the
  reviewer-response panels in `../output/scatac/ext_gse129785/` at 180 mm
  main-figure width from the same data and row order; the response-size
  versions are no longer kept here. The scIB chart names its two LEAF-1 rows
  LEAF-1 (the original called them "classifier probs") and draws them in
  LEAF-1 blue, so the coordinate bins move from blue to grey.
* `scatac_grouped_cv_auc`. It replaces `../output/scatac/donor_cv/atlas_cv_auc.png`
  and `dryad_cv_auc.png` with one two-panel supplementary figure: each cohort's
  agreement scatter, the AUC-change panels dropped. The atlas panel is coloured
  by the share of a type's cells in its largest CV group instead of by donor
  resolution (Spearman rho with the AUC change -0.62, against +0.40 for the
  number of groups the old second panel plotted). Every AUC is unchanged.

Fonts. Every panel uses leaf-1-figures' font order (Arial, DejaVu Sans,
Helvetica, Liberation Sans). Arial is not installed on this server, so PNG and
PDF output is rendered in DejaVu Sans, exactly as the published panels were; SVG
keeps text as text with Arial listed first, so it opens as Arial on a machine
that has it.

A clean re-run reproduces every PNG and every source-data TSV byte for byte.
PDF and SVG do not: matplotlib records a creation timestamp in both, so those
checksums in `FIGURE_OUTPUTS.tsv` change on every run even though the rendered
figure is identical. Re-run `make_manifests.py` after regenerating.

## Adding a figure

1. Decide its cut point and add the staging step to `../stage_data.py`.
2. Add the notebook, following the header cell of an existing one.
3. Run it, then `python figure/make_manifests.py`.
4. Add its row to `NOTEBOOK_PROVENANCE.tsv`.

## Known upstream quirk

`snapnative_mnc` carries 10,130 cells in the atlas UMAP table where every other
representation carries 10,131. One cell is dropped by SnapATAC's own
preprocessing; this comes from the analysis output and is not introduced by the
staging step.
