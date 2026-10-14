from pathlib import Path
import unittest
import pandas as pd
from src.modeling import load_station_data, run_comparison

ROOT = Path(__file__).resolve().parents[1]

class TestModeling(unittest.TestCase):
    def test_source_schema_and_exclusions(self):
        df = load_station_data(ROOT / "data" / "station_level.csv")
        self.assertEqual(len(df), 51)
        self.assertFalse(df["start_station_name"].isin(["Grove St PATH", "Liberty Light Rail"]).any())

    def test_model_evaluates(self):
        df = load_station_data(ROOT / "data" / "station_level.csv")
        result, y_test, predictions = run_comparison(df)
        self.assertEqual(len(result), 3)
        self.assertTrue(pd.notna(result["test_mae"]).all())
        self.assertEqual(len(y_test), len(predictions["Mean baseline"]["predictions"]))

if __name__ == "__main__":
    unittest.main()
