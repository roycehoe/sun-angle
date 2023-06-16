# Reference: https://www.omnicalculator.com/physics/sun-angle

from dataclasses import dataclass
from typing import Any


@dataclass
class SunAngleVariables:
    azimuth: Any
    elevation: Any


def get_declination_angle(day_of_year: int):
    ...


def get_local_hour_angle(local_solar_time):
    ...


def get_elevation(declination_angle, latitude, local_hour_angle):
    ...


def get_azimuth(declination_angle, latitude, local_hour_angle):
    ...
