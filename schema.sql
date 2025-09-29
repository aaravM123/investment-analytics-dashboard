-- Users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- Transactions
CREATE TABLE transactions (
    txn_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    ticker VARCHAR(10),
    txn_type VARCHAR(4) CHECK (txn_type IN ('BUY','SELL')),
    quantity NUMERIC,
    price NUMERIC,
    txn_date DATE
);

-- Prices
CREATE TABLE prices (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10),
    date DATE,
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    volume BIGINT
);
