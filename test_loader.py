import pandas as pd
import unittest
from loader import *

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        expected = [
            {"location": "Museum of Modern Art",
             "latitude": 40.7618552, "longitude": -73.9782438,
             "type": "museum"},
            {"location": "USS Alabama Battleship Memorial Park",
             "latitude": 30.684373, "longitude": -88.015316,
             "type": "park"},
        ]

        geo = get_geolocator()
        df = build_geo_dataframe(geo, [row["location"] for row in expected])

        self.assertEqual(len(df), len(expected),
                         "Every location should produce exactly one row.")

        for i, row in enumerate(expected):
            actual = df.iloc[i]

            self.assertEqual(actual["location"], row["location"],
                             "Rows should stay in the order requested.")

            for coord in ["latitude", "longitude"]:
                self.assertAlmostEqual(
                    actual[coord], row[coord], places=2,
                    msg=f"{row['location']} has an unexpected {coord}.")

            self.assertEqual(actual["type"].lower(), row["type"],
                             f"{row['location']} has an unexpected type.")

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertEqual(result["location"], "asdfqwer1234",
                         "A nonexistent location should still keep its name.")

        for field in ["latitude", "longitude", "type"]:
            self.assertTrue(
                pd.isna(result[field]),
                f"A nonexistent location should have NA for {field}.")

if __name__ == "__main__":
    unittest.main()
