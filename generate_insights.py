import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from openai import OpenAI

# Load env vars
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

engine = create_engine(DATABASE_URL)
client = OpenAI(api_key=OPENAI_API_KEY)

def fetch_view(view_name: str) -> pd.DataFrame:
    with engine.connect() as conn:
        return pd.read_sql(f"SELECT * FROM {view_name};", conn)

if __name__ == "__main__":
    # Fetch data
    portfolio_value = fetch_view("portfolio_value")
    profit_loss = fetch_view("portfolio_profit_loss")

    if profit_loss.empty:
        print("No profit/loss data available. Did you seed prices?")
        exit()

    # Format raw summary
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

    print("\nRaw Summary (for AI):\n", summary_text)

    # --- Call OpenAI ---
    prompt = f"""
    You are a financial analyst. Based on this portfolio data, write a short summary of performance,
    risks, and highlights in plain English:

    {summary_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    ai_insight = response.choices[0].message.content
    print("\nAI-Generated Insight:\n")
    print(ai_insight)
