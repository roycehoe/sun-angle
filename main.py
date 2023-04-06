from dataclasses import dataclass

from dotenv import dotenv_values

env_values = dotenv_values()
WINDOW_DIRECTION = env_values.get("WINDOW_DIRECTION")
LATITUDE = env_values.get("LATITUDE")
LONGITUDE = env_values.get("LONGITUDE")
ELEVATION = env_values.get("ELEVATION")
