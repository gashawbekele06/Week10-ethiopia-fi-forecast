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

week10-ethiopia-fi-forecast/
├── data/
│ ├── raw/ # Starter dataset (.xlsx)
│ └── processed/ # Enriched CSV from Task 1
├── notebooks/
│ ├── task1_data_exploration_and_enrichment.ipynb
│ └── task2_eda.ipynb
├── src/
│ └── data_loader.py # OOP class for loading/exploring/enriching
├── requirements.txt
├── data_enrichment_log.md
└── README.md

## Completed Tasks

### Task 1: Data Exploration and Enrichment

- Loaded and explored unified schema (observations, events, impact_links).
- Enriched with high-confidence 2025 data:
  - Telebirr registered users (54.84M, July 2025)
  - M-Pesa 90-day active users (5M, Dec 2025)
  - 4G towns coverage (1,030 towns, Dec 2025)
  - NDPS 2026–2030 policy launch
- Saved enriched dataset to `data/processed/`
- Documented additions in `data_enrichment_log.md`

### Task 2: Exploratory Data Analysis

- Dataset overview: record_type distribution, temporal coverage, confidence levels.
- Access trajectory (2011–2024): visualized slowdown (+3pp 2021–2024).
- Usage vs registered gap analysis.
- Infrastructure/enablers trends.
- Events overlay on access trajectory.
- Correlation heatmap of indicators.
- 6 key insights with evidence (slowdown explained by active gap, infrastructure as leading indicator, event impacts, data gaps, hypotheses).

## Setup & Installation

````bash
# Clone repo (if not already)
git clone <your-repo-url>
cd Week10-ethiopia-fi-forecast

# Recommended: uv for fast env (or pip)
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv sync  # or pip install -r requirements.txt

# Install openpyxl for Excel loading
pip install openpyxl


Copy this content into your project's `README.md` file in the root directory.

Commit:
```bash
git add README.md
git commit -m "Add comprehensive README.md with project goal, objectives, Task 1-2 summary, setup instructions"
git push origin main
````
