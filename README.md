# Ethiopia Financial Inclusion Forecasting

## Overview

Ethiopia is undergoing a rapid digital financial transformation, with mobile money platforms like Telebirr (54M+ users) and M-Pesa driving registration growth. However, the 2024 Global Findex survey shows only 49% adult account ownership (+3pp since 2021) and limited active usage, highlighting a significant registered vs. active gap.

This project develops a forecasting system to track and predict Ethiopia's progress on the two core dimensions of financial inclusion as defined by the World Bank's Global Findex:

1. **Access** — Account Ownership Rate
2. **Usage** — Digital Payment Adoption Rate

## Project Goal

Build a data-driven forecasting system that models how policies, product launches, infrastructure investments, and market events affect financial inclusion outcomes in Ethiopia, enabling stakeholders to understand drivers and predict progress toward national targets.

## Project Objectives

- Understand and enrich the unified financial inclusion dataset with recent 2025 data (operator reports, infrastructure, policy events).
- Analyze historical patterns, slowdowns, and the registered vs. active gap.
- Model event impacts on key indicators.
- Forecast Access and Usage rates for 2025–2027 under different scenarios.
- Deliver findings through interactive visualizations and a Streamlit
  dashboard.

## Data

- **Starter Dataset**: `data/raw/ethiopia_fi_unified_data.xlsx` (unified schema with observations, events, impact_links, targets)
- **Reference Codes**: `data/raw/reference_codes.xlsx`
- **Enriched Dataset**: `data/processed/ethiopia_fi_unified_data_enriched.csv` (Task 1 output with 2025 additions: Telebirr 54.84M users, M-Pesa 5M active, 4G expansion, NDPS launch)
- **Enrichment Log**: `data_enrichment_log.md`

## Project Structure

ethiopia-fi-forecast/
├── .github/workflows/ # CI unittests (pip-based)
├── data/
│ ├── raw/ # Starter unified.xlsx + reference_codes.xlsx
│ └── processed/ # Enriched CSV from Task 1
├── dashboard/
│ └── app.py # Streamlit interactive dashboard
├── notebooks/
│ ├── task1_data_exploration_and_enrichment.ipynb
│ ├── task2_eda.ipynb
│ ├── task3_modeling.ipynb
│ └── task4_forecasting.ipynb
├── src/
│ └── data_loader.py # OOP class for loading/exploring/enriching
├── requirements.txt
├── data_enrichment_log.md
└── README.md

## Completed Tasks

- **Task 1**: Data exploration, enrichment with 2025 records (Telebirr 54.84M, M-Pesa 5M active, 4G 1,030 towns, NDPS launch), saved processed CSV, log.
- **Task 2**: EDA with trajectory plots, registered vs active gap, events overlay, correlation heatmap, 6 key insights, data limitations section.
- **Task 3**: Manual event-impact association matrix (no impact_links in starter), refinements from comparables (Kenya M-Pesa adjusted), validation, methodology.
- **Task 4**: Baseline trend + event-augmented forecasts 2025–2027, scenarios (base/optimistic/pessimistic), confidence intervals, interpretation.
- **Task 5**: Streamlit dashboard with Overview, Trends, Forecasts, Inclusion Projections pages (4+ interactive visualizations, metrics, download).

## Setup & Installation

`````bash
git clone https://github.com/gashawbekele06/Week10-ethiopia-fi-forecast.git
cd Week10-ethiopia-fi-forecast

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install openpyxl  # For .xlsx loading
pip install streamlit plotly  # Dashboard


## Running the Dashboard

````bash
streamlit run dashboard/app.py

`````
