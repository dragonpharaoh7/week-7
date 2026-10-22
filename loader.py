'''
Script to load geographical data into a pandas DataFrame, and save it as a
CSV file.
'''

import pandas as pd
from geopy.geocoders import Nominatim


def get_geolocator(agent='h501-student'):
    """
    Initiate a Nominatim geolocator instance given an `agent`.

    Parameters
    ----------
    agent : str, optional
        Agent name for Nominatim, by default 'h501-student'
    """
    return Nominatim(user_agent=agent)


def fetch_location_data(geolocator, loc):
    location = geolocator.geocode(loc)

    if location is None:
        return {"location": loc,
                "latitude": float("nan"),
                "longitude": float("nan"),
                "type": float("nan")}

    return {"location": loc,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "type": location.raw.get("type")}


def build_geo_dataframe(geolocator, locations):
    geo_data = [fetch_location_data(geolocator, loc) for loc in locations]

    return pd.DataFrame(geo_data)


if __name__ == "__main__":
    geo = get_geolocator()

    locations = ["Museum of Modern Art", "iuyt8765(*&)", "Alaska",
                 "Franklin's Barbecue", "Burj Khalifa"]

    df = build_geo_dataframe(geo, locations)

    df.to_csv("./geo_data.csv")
