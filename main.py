from dotenv import dotenv_values

env_values = dotenv_values()
POSTAL_CODE = env_values.get("POSTAL_CODE")
