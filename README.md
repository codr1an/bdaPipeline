# Big Data Analysis: Cryptocurrency Pipeline

## Goal

The goal of this project is the development of a data pipeline prototype that includes data ingestion, processing and visualization.

## TL;DR Requirements and Startup

**Python 3.11.3** (The project was developed in this version however some older versions will probably suffice)

**Libraries:** requests, pandas, gradio, plotly

Installation Linux/MacOS (for Windows add `py -m` before):

```
pip install requests pandas gradio plotly
```

Startup:

```
cd bdaPipeline/

py data_pipeline_main.py
```

## Requirements

- Data Ingestion:

  - API Call
  - Data Stream (Wikipedia live changes, ...)
  - Data from file uploads (if other options are not possible)

- Data Storage

  - in NoSQL/relational Databases or direct processing

- Data Processing, Analysis and Visualisation
  - Presentation of the results with simple visualisation (e.g.: Jupyter, Streamlit or gradio)

## Approach

**Theme**: Crypto currency analysis

**Data Source** : https://docs.coincap.io/

**Data Ingestion**: API Calls

**Data Storage**: Data will not be stored in a database, instead it will be directly processed with **_Pandas_** (https://pandas.pydata.org/)

**Data Processing, Analysis and Visualisation**: Data visualisation will be done with **_Gradio_** (https://www.gradio.app/) for the plots I will use **_Plotly_** (https://plotly.com/)

## Libraries

Following libraries are needed for the project to work: requests, pandas, gradio and plotly

Installation Linux/MacOS:

```
pip install requests pandas gradio plotly
```

Installation Windows:

```
py -m pip install requests pandas gradio plotly
```

## Startup

After cloning the repository, write these commands in your bash terminal in order to start the pipeline:

```
cd bdaPipeline/

py data_pipeline_main.py
```

A browser window should open, if this is not the case either press on the link presented in your terminal or access http://127.0.0.1:7860 in your browser.

In order to stop the pipeline either press `ctrl + c` in the terminal or simply close it.
