# Portfolio Analytics

A comprehensive portfolio analytics system that tracks investment transactions, calculates portfolio values, and provides AI-powered insights through both command-line tools and a web dashboard.

## Features

- **Transaction Tracking**: Record buy/sell transactions with timestamps
- **Portfolio Valuation**: Real-time portfolio value calculation using current market prices
- **Profit/Loss Analysis**: Track investment performance and returns
- **AI-Powered Insights**: Generate intelligent portfolio analysis using OpenAI GPT-4
- **Interactive Dashboard**: Web-based interface built with Streamlit
- **Database Views**: Optimized SQL views for efficient data retrieval

## Architecture

### Database Schema

The system uses PostgreSQL with the following core tables:

- **users**: User account information
- **transactions**: Buy/sell transaction records
- **prices**: Historical stock price data

### SQL Views

The system includes several analytical views:

- `current_holdings`: Net share positions per user/ticker
- `portfolio_cost_basis`: Total investment amount per position
- `latest_prices`: Most recent price data for each ticker
- `portfolio_value`: Current market value of all positions
- `portfolio_profit_loss`: Profit/loss analysis for each position

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL database
- OpenAI API key

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio-analytics
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pandas sqlalchemy psycopg2-binary python-dotenv streamlit openai
```

4. Set up environment variables:
Create a `.env` file in the project root:
```
DATABASE_URL=postgresql://username:password@localhost:5432/portfolio_db
OPENAI_API_KEY=your_openai_api_key_here
```

5. Initialize the database:
```bash
psql -d portfolio_db -f schema.sql
psql -d portfolio_db -f sample_data.sql
psql -d portfolio_db -f prices_seed.sql
psql -d portfolio_db -f analytics.sql
```

## Usage

### Command Line Tools

#### Database Connection Test
```bash
python db_connect.py
```
Tests the database connection and displays current server time.

#### Portfolio Analytics Query
```bash
python analytics_query.py
```
Displays current holdings, portfolio value, and profit/loss data in tabular format.

#### AI-Powered Insights
```bash
python generate_insights.py
```
Generates a formatted portfolio summary and uses OpenAI to provide intelligent analysis and recommendations.

### Web Dashboard

Launch the interactive Streamlit dashboard:
```bash
streamlit run dashboard.py
```

The dashboard provides:
- Current holdings table
- Portfolio value summary
- Profit/loss analysis
- AI-generated insights (click "Generate Insights" button)

## File Structure

```
portfolio-analytics/
├── schema.sql              # Database table definitions
├── sample_data.sql         # Sample user and transaction data
├── prices_seed.sql         # Sample stock price data
├── analytics.sql           # SQL views for analytics
├── db_connect.py           # Database connection utility
├── analytics_query.py      # Command-line portfolio query tool
├── generate_insights.py    # AI-powered insights generator
├── dashboard.py            # Streamlit web dashboard
└── README.md              # This file
```

## API Integration

### OpenAI Integration

The system integrates with OpenAI's GPT-4 model to provide intelligent portfolio analysis. The AI analyzes:
- Portfolio performance trends
- Risk assessment
- Investment recommendations
- Market insights

### Database Integration

Uses SQLAlchemy for database connectivity and pandas for data manipulation, providing a robust foundation for financial data processing.

## Data Flow

1. **Transaction Recording**: Users record buy/sell transactions
2. **Price Updates**: Current market prices are stored in the prices table
3. **View Calculation**: SQL views automatically calculate holdings, values, and P&L
4. **Analysis**: Python scripts query views and format data for display
5. **AI Processing**: Portfolio data is sent to OpenAI for intelligent analysis
6. **Presentation**: Results are displayed via command-line or web dashboard

## Configuration

### Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `OPENAI_API_KEY`: OpenAI API key for AI insights

### Database Configuration

Ensure your PostgreSQL database is configured to accept connections and has sufficient privileges for the application user.

## Dependencies

- **pandas**: Data manipulation and analysis
- **sqlalchemy**: Database ORM and connection management
- **psycopg2-binary**: PostgreSQL database adapter
- **python-dotenv**: Environment variable management
- **streamlit**: Web dashboard framework
- **openai**: OpenAI API client

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.