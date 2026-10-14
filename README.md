# Jersey City Citi Bike — Spatial Equity & Demand Forecasting

**Python · Data science · Transportation equity · WCTR 2026**

A reproducible companion to my research on bike-share accessibility and station demand in Jersey City, New Jersey, presented at the **2026 World Conference on Transport Research (WCTR), Toulouse**.

## Why this matters

Bike-share stations are not distributed evenly. This project explores the relationship between ridership, neighborhood population and income, and the limitations of forecasting demand at underserved locations. The research also included a GIS walking-accessibility component; the supplied code repository focuses on the Python modeling component.

## Start here

```bash
git clone https://github.com/nealpuri704/jersey-city-citibike-demand-forecasting.git
cd jersey-city-citibike-demand-forecasting
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Open **`notebooks/01_reproducible_analysis.ipynb`** and run all cells. The notebook works when launched from the root or `notebooks/` folder.

Run automated checks:

```bash
python -m unittest discover -s tests -v
```

## What you will find

| Path | Content |
| --- | --- |
| `notebooks/01_reproducible_analysis.ipynb` | Clean tutorial, visuals and reproducible held-out model comparison |
| `src/modeling.py` | Reusable data loader and regression comparison functions |
| `data/` | Monthly and station-level datasets supplied by the author |
| `research_archive/` | Five original AP Research / WCTR-era notebooks (historical working files) |
| `tests/` | Basic data and modeling checks |

## The historical R² ≈ 0.51 — an important distinction

The original notebook `research_archive/AP Research 3 (with month and Grove St).ipynb` (code cell index 8, zero-based) contains saved output **R² = 0.5107** for a quadratic regression using log population, log income and their interaction after excluding selected stations. This was an **in-sample fit**, not a held-out test estimate. That cell depends on an intermediate input CSV **`nlls_predictions_with_two_independent_sqrt_nogrovest330.csv`**, which is *not included* in the supplied files, so the original number cannot currently be independently reproduced by running that cell from scratch.

**Do not confuse that historical figure with new model performance.** The main notebook fits a fresh baseline/linear/quadratic-Ridge comparison to the available station-level CSV with a held-out station split and reports its own separate scores. It does not claim identical estimates to the historical paper.

## Dataset notes

- `data/filtered_dataset.csv`: **636 station-month observations**, 53 stations × 12 months.
- `data/station_level.csv`: **53 station-level observations**, including origin/destination counts, demographics, and log/sqrt features.
- Main notebook excludes Grove St PATH, Liberty Light Rail, and Hoboken Ave and Monmouth St when present, matching the historical explicit exclusion list. The supplied station dataset includes the first two, yielding **51 modeling rows**.
- **Scope and limitations:** these data alone cannot reconstruct walking isochrones, station-site proposals, or the complete original preprocessing of raw Citi Bike trip data. Census geography selection, station/demographic joins, and dataset provenance should be audited before making policy or investment decisions. The repository uses provided CSVs as supplied rather than claiming they are newly verified source data.

## What you can reuse

`src/modeling.py` accepts station-level CSVs with `start_station_name`, `number_of_origins`, `log_population`, and `log_income`. Adapt exclusion logic and feature definitions for your city, evaluate on held-out stations, and add network/accessibility features before using it for real station siting. Dataset formats and feature engineering are described in the notebook.

## Research attribution

**Neal Puri**, *Spatial Equity and Demand Forecasting for the Citi Bike Program in Jersey City*, research presented at WCTR 2026 (Toulouse, France). This repository is a cleaned companion and archival release, **not** an independent certification of the presentation results.

## License

MIT license covers the new repository code. Third-party Citi Bike/Census datasets remain subject to their original terms. Please cite the research if you reuse results. No guarantee of operational forecasting accuracy.