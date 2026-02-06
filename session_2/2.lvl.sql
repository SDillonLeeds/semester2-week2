-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit



SELECT email, SUM(total_amount) FROM (
    Customers JOIN Orders ON (Customers.customer_id=Orders.customer_id)
) GROUP BY email ORDER BY total_amount DESC LIMIT 5;