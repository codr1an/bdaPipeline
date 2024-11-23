import gradio as gr
from data_visualization import visualize_top_10, visualize_trends, visualize_all_trends
from data_processing import process_data


def main():
    def display_table_and_plot():
        table, plot = visualize_top_10()
        return table, plot

    def display_trend(crypto_id, period):
        trend_table, trend_plot = None, None

        if crypto_id == "All":
            trend_table, trend_plot = visualize_all_trends(period)
        else:
            trend_table, trend_plot = visualize_trends(crypto_id, period)

        return trend_table, trend_plot

    with gr.Blocks() as demo:
        gr.Markdown("# Big Data Analyisis: Cryptocurrency")

        with gr.Tab("Top 10"):
            table = gr.Dataframe(label="Top 10 Cryptocurrencies")
            plot = gr.Plot(label="Top 10 Cryptocurrencies by Price (EUR)")

        with gr.Tab("Trends"):
            top_10_data = process_data()
            crypto_id = gr.Dropdown(
                label="Cryptocurrency ID",
                choices=["All"] + top_10_data["id"].tolist(),
                value="All",
            )

            period = gr.Radio(
                label="Period", choices=["30 Days", "12 Months"], value="30 Days"
            )
            trend_table = gr.Dataframe(label="Trend Data")
            trend_plot = gr.Plot(label="Price Trend (EUR)")
            btn_trend = gr.Button("Fetch Trend")
            btn_trend.click(
                display_trend,
                inputs=[crypto_id, period],
                outputs=[trend_table, trend_plot],
            )

        demo.load(display_table_and_plot, outputs=[table, plot])
        demo.launch(share=False, inbrowser=True)

    demo.launch()


if __name__ == "__main__":
    main()
