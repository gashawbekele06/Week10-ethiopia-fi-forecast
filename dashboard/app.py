# dashboard/app.py
# Streamlit Dashboard for Ethiopia Financial Inclusion Forecasting
# Run with: streamlit run dashboard/app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Project root (adjust if needed)
project_root = Path(__file__).parent.parent

# Load enriched dataset
enriched_path = project_root / "data" / "processed" / \
    "ethiopia_fi_unified_data_enriched.csv"
df = pd.read_csv(enriched_path)

# Parse dates
date_cols = ['observation_date', 'event_date', 'date']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Hardcoded Findex for trajectory (robust)
findex_access = pd.DataFrame({
    'Year': [2011, 2014, 2017, 2021, 2024],
    'Account Ownership (%)': [14.0, 22.0, 35.0, 46.0, 49.0]
})

# Forecast from Task 4 (example values – replace with your model output)
forecast_df = pd.DataFrame({
    'Year': [2025, 2026, 2027],
    'Access Base (%)': [55.0, 60.0, 65.0],
    'Access Lower CI': [50.0, 55.0, 60.0],
    'Access Upper CI': [60.0, 65.0, 70.0],
    'Usage Base (%)': [25.0, 35.0, 45.0],
    'Usage Lower CI': [20.0, 30.0, 40.0],
    'Usage Upper CI': [30.0, 40.0, 50.0]
})

# App config
st.set_page_config(page_title="Ethiopia FI Forecast Dashboard", layout="wide")
st.title("Ethiopia Financial Inclusion Forecasting Dashboard")
st.markdown(
    "Interactive exploration of historical trends, event impacts, and 2025–2027 forecasts.")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Select Page", ["Overview", "Trends", "Forecasts", "Inclusion Projections"])

if page == "Overview":
    st.header("Overview & Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Latest Account Ownership (2024)", "49%", "+3pp since 2021")
    col2.metric("Registered Users (2025 est.)", "55M+", "Telebirr + M-Pesa")
    col3.metric("Active Users (2025 est.)", "5M+", "M-Pesa 90-day")
    col4.metric("4G Towns Coverage (2025)", "1,030", "Major infra leap")

    st.markdown(
        "**P2P/ATM Crossover Ratio** (placeholder – data not in unified schema)")
    st.info("P2P transactions dominate; merchant/ATM use low – explains active gap. (Source: Market Nuances guide)")

    st.markdown("**Growth Highlights**")
    st.write("- Pre-2021: Rapid +11pp growth")
    st.write("- Post-2021: Slow +3pp despite registration surge")

if page == "Trends":
    st.header("Historical Trends")
    st.subheader("Account Ownership Trajectory (Findex 2011–2024)")
    fig_traj = px.line(findex_access, x='Year', y='Account Ownership (%)', markers=True,
                       title='Account Ownership Trajectory')
    fig_traj.update_yaxes(range=[0, 100], ticksuffix='%')
    st.plotly_chart(fig_traj, use_container_width=True)

    st.subheader("Events Overlay")
    # Events from dataset
    events = df[df['record_type'] == 'event']
    fig_events = px.line(findex_access, x='Year',
                         y='Account Ownership (%)', markers=True)
    for _, event in events.iterrows():
        if pd.notna(event.get('event_date')):
            event_year = pd.to_datetime(event['event_date']).year
            fig_events.add_vline(x=event_year, line_dash="dash", annotation_text=event.get(
                'description', 'Event')[:30])
    st.plotly_chart(fig_events, use_container_width=True)

    st.subheader("Data Download")
    st.download_button("Download Enriched Dataset", df.to_csv(
        index=False), "ethiopia_fi_enriched.csv", "text/csv")

if page == "Forecasts":
    st.header("2025–2027 Forecasts")
    scenario = st.selectbox(
        "Select Scenario", ["Base", "Optimistic", "Pessimistic"])

    if scenario == "Base":
        access_col = 'Access Base (%)'
        usage_col = 'Usage Base (%)'
    elif scenario == "Optimistic":
        access_col = 'Access Upper CI'
        usage_col = 'Usage Upper CI'
    else:
        access_col = 'Access Lower CI'
        usage_col = 'Usage Lower CI'

    fig_forecast = go.Figure()
    fig_forecast.add_trace(go.Scatter(
        x=forecast_df['Year'], y=forecast_df[access_col], mode='lines+markers', name='Access Forecast'))
    fig_forecast.add_trace(go.Scatter(
        x=forecast_df['Year'], y=forecast_df[usage_col], mode='lines+markers', name='Usage Forecast'))
    fig_forecast.update_layout(
        title=f'{scenario} Scenario Forecast', yaxis_title='Percentage (%)')
    st.plotly_chart(fig_forecast, use_container_width=True)

    st.write("**Key Projected Milestones** (Base scenario):")
    st.write("- 2026: Access ~60% (NDPS effect)")
    st.write("- 2027: Usage ~35-40% if active gap narrows")

if page == "Inclusion Projections":
    st.header("Progress Toward 60% Target")
    target = 60
    st.metric("National Target (NFIS-II)",
              f"{target}% Account Ownership by 2025")

    # Fixed: Use pd.concat instead of deprecated append
    historical = findex_access.copy()
    historical = historical.rename(
        columns={'Account Ownership (%)': 'Account Ownership (%)'})

    forecast_projection = forecast_df[['Access Base (%)']].copy()
    forecast_projection = forecast_projection.rename(
        columns={'Access Base (%)': 'Account Ownership (%)'})

    # Concat historical + forecast
    progress_data = pd.concat([historical, forecast_projection])
    progress_data = progress_data.reset_index()  # Year as column

    progress_fig = px.line(progress_data, x='Year', y='Account Ownership (%)', markers=True,
                           title='Progress Toward 60% Account Ownership Target')
    progress_fig.add_hline(y=target, line_dash="dash", line_color="red",
                           annotation_text="60% Target", annotation_position="top right")

    # Extend line to 2027
    progress_fig.update_xaxes(range=[2011, 2027])
    progress_fig.update_yaxes(range=[0, 100], ticksuffix='%')

    st.plotly_chart(progress_fig, use_container_width=True)

    st.write("**Answers to Key Questions**")
    st.write(
        "- **Drive inclusion?** Active usage activation, interoperability (NDPS), infrastructure.")
    st.write(
        "- **Stagnation cause?** Registered vs active gap (P2P dominance, low merchant adoption).")
    st.write("- **Gender gap?** Not in data – limitation.")
    st.write(
        "- **Gaps limiting analysis?** Sparse Findex, no disaggregation, post-2024 enriched.")

st.sidebar.markdown("### Run Instructions")
st.sidebar.info("Run locally: `streamlit run dashboard/app.py`")
