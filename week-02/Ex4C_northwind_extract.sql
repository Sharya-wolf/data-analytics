USE northwind;
SELECT * FROM employees;
-- The employee that makes her name look like a bird is Margaret Peacock--
SELECT * FROM products;
-- The query return 77 records--
-- By using limit to--
SELECT * FROM products LIMIT 10;
SELECT * FROM categories;
-- The category ID for seafood is 8--
SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders LIMIT 50;