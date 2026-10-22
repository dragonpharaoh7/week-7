import pandas as pd
import unittest
from loader import *

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        # your code here
        return None

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertEqual(result["location"], "asdfqwer1234",
                         "A nonexistent location should still keep its name.")

        for field in ["latitude", "longitude", "type"]:
            self.assertTrue(pd.isna(result[field]),
                            f"A nonexistent location should have NA for {field}.")

if __name__ == "__main__":
    unittest.main()
