import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    layout="wide"
)

st.title("📊 Mutual Fund Analytics Dashboard")

performance_metrics = pd.read_csv("performance_metrics.csv")
recommended_funds = pd.read_csv("recommended_funds.csv")

# KPI Section
col1, col2, col3 = st.columns(3)

col1.metric(
    "Funds Analysed",
    len(performance_metrics)
)

col2.metric(
    "Avg CAGR",
    round(performance_metrics["cagr"].mean()*100, 2)
)

col3.metric(
    "Avg Sharpe Ratio",
    round(performance_metrics["sharpe_ratio"].mean(), 2)
)

st.divider()

# Risk vs Return
st.subheader("Risk vs Return")

fig = px.scatter(
    performance_metrics,
    x="annual_volatility",
    y="annual_return",
    hover_data=["amfi_code"]
)

st.plotly_chart(fig, use_container_width=True)

# Top CAGR Funds
st.subheader("Top 10 Funds by CAGR")

top_cagr = performance_metrics.sort_values(
    "cagr",
    ascending=False
).head(10)

fig2 = px.bar(
    top_cagr,
    x="amfi_code",
    y="cagr"
)

st.plotly_chart(fig2, use_container_width=True)

# Recommended Funds
st.subheader("Recommended Funds")

st.dataframe(
    recommended_funds,
    use_container_width=True
)
st.subheader("🏆 Top Recommended Funds")

st.dataframe(
    recommended_funds,
    width="stretch"
)

st.metric(
    "Recommended Funds",
    len(recommended_funds)
)
