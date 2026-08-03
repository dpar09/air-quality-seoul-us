import os
from dotenv import load_dotenv

load_dotenv()

airnow_api = os.environ.get("AIRNOW_API_KEY")
waqi_api = os.environ.get("WAQI_API_TOKEN")

if airnow_api is None:
    raise ValueError("AIRNOW_API_KEY not found - check your .env file")

if waqi_api is None:
    raise ValueError("WAQI_API_TOKEN not found - check your .env file")

AIRNOW_BASE_URL = "https://www.airnowapi.org/aq/observation/zipCode/current/"
WAQI_BASE_URL = "https://api.waqi.info/feed/"