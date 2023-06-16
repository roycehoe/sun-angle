# Reference: https://www.omnicalculator.com/physics/sun-angle

from dataclasses import dataclass
from math import acos, asin, cos, sin
from typing import Any


@dataclass
class SunAngleVariables:
    azimuth: Any
    elevation: Any


def get_declination_angle(day_of_year: int):
    ...


def get_local_hour_angle(local_solar_time):
    ...


def get_elevation(
    declination_angle: float, latitude: float, local_hour_angle: float
) -> float:
    return asin(
        sin(declination_angle) * sin(latitude)
        + cos(declination_angle) * cos(latitude) * cos(local_hour_angle)
    )


def get_solar_azimuth(
    declination_angle: float, latitude: float, local_hour_angle: float
):
    """Calculates solar azimuth, typically not used"""
    elevation = get_elevation(declination_angle, latitude, local_hour_angle)
    return acos(
        (
            (sin(declination_angle) * cos(latitude))
            - cos(declination_angle) * sin(latitude) * cos(local_hour_angle)
        )
        / cos(elevation)
    )


def get_azimuth(declination_angle: float, latitude: float, local_hour_angle: float):
    """Calculates compass azimuth, typically used everywhere"""
    solar_azimuth = get_solar_azimuth(declination_angle, latitude, local_hour_angle)
    if local_hour_angle <= 0:
        return solar_azimuth
    return 360 - solar_azimuth
