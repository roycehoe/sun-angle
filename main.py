from dataclasses import dataclass
from datetime import datetime

from dotenv import dotenv_values
from suncalc import get_position

env_values = dotenv_values()
WINDOW_DIRECTION = env_values.get("WINDOW_DIRECTION")
LATITUDE = float(env_values.get("LATITUDE"))
LONGITUDE = float(env_values.get("LONGITUDE"))
ELEVATION = env_values.get("ELEVATION")


@dataclass
class SunPosition:
    azimuth: float
    altitude: float


def get_sun_position(lon: float, lat: float, date=datetime.now()) -> SunPosition:
    date = datetime.now()
    return SunPosition(**get_position(date, lon, lat))


print(get_sun_position(LONGITUDE, LATITUDE))
