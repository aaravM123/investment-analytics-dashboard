import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# Load env vars
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# DB + OpenAI clients
engine = create_engine(DATABASE_URL)
client = OpenAI(api_key=OPENAI_API_KEY)

def fetch_view(view_name: str) -> pd.DataFrame:
    with engine.connect() as conn:
        return pd.read_sql(f"SELECT * FROM {view_name};", conn)

def generate_ai_insight() -> str:
    """Fetches portfolio data and returns an AI-written summary."""
    portfolio_value = fetch_view("portfolio_value")
    profit_loss = fetch_view("portfolio_profit_loss")

    if profit_loss.empty:
        return "No profit/loss data available. Did you seed prices?"

    total_value = portfolio_value["market_value"].sum()
    summary_lines = [f"Total Portfolio Value: ${total_value:,.2f}\n"]

    for _, row in profit_loss.iterrows():
        summary_lines.append(
            f"{row['ticker']}: {row['net_shares']} shares, "
            f"invested ${row['net_investment']:.2f}, "
            f"now worth ${row['market_value']:.2f}, "
            f"profit/loss = ${row['profit_loss']:.2f}"
        )

    summary_text = "\n".join(summary_lines)

    # Call OpenAI
    prompt = f"""
    You are a financial analyst. Based on this portfolio data, write a concise summary 
    of performance, risks, and highlights in plain English:

    {summary_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content

# --- Streamlit App ---
st.title("Portfolio Analytics Dashboard")

# Current Holdings
st.subheader("Current Holdings")
st.dataframe(fetch_view("current_holdings"))

# Portfolio Value
st.subheader("Portfolio Value")
value = fetch_view("portfolio_value")
st.dataframe(value)

if not value.empty:
    total_value = value["market_value"].sum()
    st.metric("Total Portfolio Value", f"${total_value:,.2f}")

# Profit / Loss
st.subheader("Profit / Loss")
st.dataframe(fetch_view("portfolio_profit_loss"))

# Insights Section
st.subheader("AI Insights")
if st.button("Generate Insights"):
    with st.spinner("Analyzing portfolio..."):
        ai_report = generate_ai_insight()
    st.success("Analysis complete!")
    st.write(ai_report)
