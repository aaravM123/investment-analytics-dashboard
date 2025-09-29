INSERT INTO users (name, email) VALUES ('Aarav', 'aarav@example.com');

INSERT INTO transactions (user_id, ticker, txn_type, quantity, price, txn_date)
VALUES 
(1, 'AAPL', 'BUY', 10, 150, '2024-09-01'),
(1, 'AAPL', 'BUY', 5, 160, '2024-09-15'),
(1, 'MSFT', 'BUY', 8, 300, '2024-10-01'),
(1, 'AAPL', 'SELL', 3, 170, '2024-10-10');
