-- Current Holdings
CREATE OR REPLACE VIEW current_holdings AS
SELECT 
    t.user_id,
    t.ticker,
    SUM(CASE WHEN txn_type = 'BUY' THEN quantity ELSE -quantity END) AS net_shares
FROM transactions t
GROUP BY t.user_id, t.ticker;

-- Portfolio Cost Basis
CREATE OR REPLACE VIEW portfolio_cost_basis AS
SELECT 
    t.user_id,
    t.ticker,
    SUM(CASE WHEN txn_type = 'BUY' THEN quantity * price ELSE -quantity * price END) AS net_investment
FROM transactions t
GROUP BY t.user_id, t.ticker;

-- Latest Prices
CREATE OR REPLACE VIEW latest_prices AS
SELECT p.ticker, p.close, p.date
FROM prices p
JOIN (
    SELECT ticker, MAX(date) AS latest_date
    FROM prices
    GROUP BY ticker
) lp ON p.ticker = lp.ticker AND p.date = lp.latest_date;

-- Portfolio Value
CREATE OR REPLACE VIEW portfolio_value AS
SELECT 
    h.user_id,
    h.ticker,
    h.net_shares,
    lp.close AS latest_price,
    h.net_shares * lp.close AS market_value
FROM current_holdings h
JOIN latest_prices lp ON h.ticker = lp.ticker;

-- Profit/Loss
CREATE OR REPLACE VIEW portfolio_profit_loss AS
SELECT 
    cb.user_id,
    cb.ticker,
    cb.net_investment,
    pv.net_shares,
    pv.latest_price,
    pv.market_value,
    pv.market_value - cb.net_investment AS profit_loss
FROM portfolio_cost_basis cb
JOIN portfolio_value pv 
  ON cb.ticker = pv.ticker AND cb.user_id = pv.user_id;
