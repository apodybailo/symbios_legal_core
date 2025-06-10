import httpx
from functools import lru_cache
from src.settings_loader import get_settings  # noqa: F401

settings = get_settings()
BASE_URL = "https://opendatabot.com/api/v2"

@lru_cache(maxsize=256)
def get_company(edrpou: str) -> dict:
    url = f"{BASE_URL}/company/{edrpou}"
    params = {"apiKey": settings.OPENDATABOT_TOKEN}
    r = httpx.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()
