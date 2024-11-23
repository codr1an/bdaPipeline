import requests
import pandas as pd
import time
from datetime import datetime, timedelta

BASE_URL = "https://api.coincap.io/v2"


def fetch_current_top_10():
    response = requests.get(f"{BASE_URL}/assets")
    response.raise_for_status()
    data = response.json()["data"]

    return pd.DataFrame(data[:10])


def fetch_30d_trend_by_id(crypto_id):
    end = int(time.time() * 1000)
    start = int((datetime.now() - timedelta(days=31)).timestamp() * 1000)
    response = requests.get(
        f"{BASE_URL}/assets/{crypto_id}/history?interval=d1&start={start}&end={end}"
    )
    response.raise_for_status()
    data = response.json()["data"]

    return pd.DataFrame(data)


def fetch_12m_trend_by_id(crypto_id):
    end = int(time.time() * 1000)
    start = int((datetime.now() - timedelta(days=365)).timestamp() * 1000)

    response = requests.get(
        f"{BASE_URL}/assets/{crypto_id}/history?interval=d1&start={start}&end={end}"
    )
    response.raise_for_status()
    data = response.json()["data"]
    df = pd.DataFrame(data)

    df["time"] = pd.to_datetime(df["time"], unit="ms")

    monthly_data = df.resample("M", on="time").last().reset_index()

    return monthly_data


def fetch_usd_to_eur_rate():
    response = requests.get("https://api.coincap.io/v2/rates/euro")
    response.raise_for_status()
    data = response.json()["data"]
    return float(data["rateUsd"])
