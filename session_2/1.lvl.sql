-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit



--SELECT category FROM Products GROUP BY category;

--SELECT COUNT(customer_id) FROM Customers;

--SELECT order_id, email, order_date, status, total_amount FROM (
--    Customers RIGHT JOIN Orders ON (Customers.customer_id=Orders.customer_id)
--) ORDER BY email ASC;

SELECT name, price FROM Products WHERE (price<2);
