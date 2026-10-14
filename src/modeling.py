"""Regression utilities; these are new experiments, not exact WCTR reproductions."""
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

EXCLUDED_STATIONS = ("Grove St PATH", "Liberty Light Rail", "Hoboken Ave and Monmouth St")
FEATURES = ["log_population", "log_income"]
TARGET = "number_of_origins"

def load_station_data(path):
    df = pd.read_csv(path)
    missing = set(FEATURES + [TARGET, "start_station_name"]) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    df = df.loc[~df["start_station_name"].isin(EXCLUDED_STATIONS)].copy()
    df = df.dropna(subset=FEATURES + [TARGET]).reset_index(drop=True)
    if len(df) < 12:
        raise ValueError("Not enough stations to evaluate a held-out model")
    return df

def run_comparison(data, random_state=42):
    X = data[FEATURES].to_numpy()
    y = data[TARGET].to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=random_state)
    models = {
        "Mean baseline": DummyRegressor(strategy="mean"),
        "Linear regression": make_pipeline(StandardScaler(), LinearRegression()),
        "Quadratic Ridge": make_pipeline(PolynomialFeatures(degree=2, include_bias=False), StandardScaler(), Ridge(alpha=10.0)),
    }
    rows, outputs = [], {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        rows.append({"model": name, "test_r2": r2_score(y_test, pred), "test_mae": mean_absolute_error(y_test, pred), "test_rmse": np.sqrt(mean_squared_error(y_test, pred))})
        outputs[name] = {"model": model, "predictions": pred}
    return pd.DataFrame(rows).sort_values("test_mae"), y_test, outputs
