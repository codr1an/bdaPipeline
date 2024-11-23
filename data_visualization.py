import plotly.express as px
import pandas as pd
from data_ingestion import (
    fetch_30d_trend_by_id,
    fetch_12m_trend_by_id,
    fetch_usd_to_eur_rate,
)
from data_processing import process_data


def visualize_top_10():
    data = process_data()
    data["priceEurFormatted"] = data["priceEur"].apply(lambda x: f"{x:,.2f}")

    fig = px.bar(
        data,
        x="id",
        y="priceEur",
        title="Top 10 Cryptocurrencies by Price (EUR)",
        labels={"priceEur": "Price (EUR)", "id": "Cryptocurrency"},
        text="priceEurFormatted",
    )

    max_value = data["priceEur"].max()
    fig.update_layout(yaxis=dict(range=[0, max_value * 1.1]))

    return data[["id", "symbol", "priceEur"]], fig


def visualize_trends(crypto_id, period):
    usd_to_eur = fetch_usd_to_eur_rate()
    if period == "30 Days":
        trend_data = fetch_30d_trend_by_id(crypto_id)
    elif period == "12 Months":
        trend_data = fetch_12m_trend_by_id(crypto_id)

    trend_data["priceUsd"] = pd.to_numeric(trend_data["priceUsd"], errors="coerce")
    trend_data["priceEur"] = trend_data["priceUsd"] / usd_to_eur
    trend_data["date"] = pd.to_datetime(trend_data["time"], unit="ms").dt.date

    trend_data["priceEur"] = trend_data["priceEur"].round(2)

    fig = px.line(
        trend_data,
        x="date",
        y="priceEur",
        title=f"{crypto_id} Price Trend ({period}) in EUR",
        labels={"priceEur": "Price (EUR)", "date": "Date"},
        hover_data={"priceEur": ":.2f"},
        markers=True,
    )
    fig.update_traces(mode="lines+markers")
    return trend_data[["date", "priceEur"]], fig
