# Reproducibility and methodological notes

## Historical experiment

Original notebook: `research_archive/AP Research 3 (with month and Grove St).ipynb`, zero-based code cell 8. Stored output: R² 0.5107, MSE 17,065,767.6002. Uses `PolynomialFeatures(degree=2)` on log population, log income and their interaction, with `LinearRegression`, and evaluates on the same observations as fitting. Depends on an unavailable intermediate file `nlls_predictions_with_two_independent_sqrt_nogrovest330.csv`. This notebook is archived unchanged and cannot be cleanly run end-to-end from the supplied input files.

## New demonstration

The public tutorial instead uses `data/station_level.csv` (53 existing stations; 51 after historical exclusions), a fixed 75/25 train/test station split, and a mean baseline, linear regression and quadratic Ridge regression. Its holdout score is not a reproduction of historical R². No claim of predictive validity for new stations or causal impact is made.

## Data / license caution

Data from third parties may have separate redistribution terms. Verify Citi Bike and Census license / attribution requirements before broad republishing. Users should independently check geographic joins and temporal definitions.