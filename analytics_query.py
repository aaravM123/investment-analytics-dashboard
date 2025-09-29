import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# Function to query a view
def fetch_view(view_name: str):
    with engine.connect() as conn:
        df = pd.read_sql(f"SELECT * FROM {view_name};", conn)
    return df

if __name__ == "__main__":
    # Current Holdings
    holdings = fetch_view("current_holdings")
    print("\nCurrent Holdings")
    print(holdings)

    # Portfolio Value
    value = fetch_view("portfolio_value")
    print("\nPortfolio Value")
    print(value)

    # Profit/Loss
    pl = fetch_view("portfolio_profit_loss")
    print("\nPortfolio Profit/Loss")
    print(pl)
