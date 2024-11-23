import pandas as pd
from data_ingestion import fetch_current_top_10, fetch_usd_to_eur_rate


def process_data():
    usd_to_eur = fetch_usd_to_eur_rate()
    top_10 = fetch_current_top_10()
    top_10["priceUsd"] = pd.to_numeric(top_10["priceUsd"], errors="coerce")
    top_10["priceEur"] = top_10["priceUsd"] / usd_to_eur
    top_10["rank"] = pd.to_numeric(top_10["rank"], errors="coerce")
    top_10 = top_10.sort_values(by="rank").reset_index(drop=True)

    top_10["priceEur"] = top_10["priceEur"].round(2)

    return top_10
