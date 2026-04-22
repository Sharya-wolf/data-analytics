-- Sha'Rya Weaver--
-- April 20, 2026--
SHOW DATABASES;
USE northwind;
SHOW TABLES;
SELECT table_name 
FROM information_schema.tables
WHERE table_schema = 'northwind'
AND table_type = 'Base Table';
SELECT ProductName, UnitPrice From products;
SELECT * FROM products;
SELECT ProductName AS 'Product',
 UnitPrice AS 'Price(USD)',
 UnitsInStock AS 'Stock'
 FROM products;
 SELECT CompanyName, City, Country
 FROM Customers
 WHERE Country = 'Germany';
 SELECT ProductName, UnitPrice
 FROM products
 WHERE UnitPrice > '50';
 SELECT OrderID, CustomerID, ShipCountry, Freight
 FROM Orders
 WHERE ShipCountry = 'France';
 SELECT ProductName, UnitsInStock, ReorderLevel
 FROM products
 WHERE UnitsInStock < ReorderLevel;
 SELECT OrderID, Freight
 FROM Orders
 WHERE Freight >= '100';
 SELECT UnitPrice, UnitsInStock
 FROM productS
 WHERE UnitPrice > '20' AND UnitsInStock > '50';
 SELECT CompanyName, Country
 FROM Customers
 WHERE Country = 'UK' OR 'Ireland';
 SELECT CategoryID, UnitPrice
 FROM products
 WHERE (CategoryID = '1' OR '2') 
 AND UnitPrice < '20';
 SELECT CompanyName, Country
 FROM Customers
 WHERE NOT Country = 'U.S.A'; 
 SELECT ProductName
 FROM products
 WHERE NOT Discontinued = '1';
 SELECT CompanyName, Country
 FROM Customers 
 WHERE Country IN ('France', 'Germany', 'Spain');
 SELECT ProductName, SupplierID
 FROM products
 WHERE SupplierID NOT IN (1, 2, 3);
 SELECT ProductName, UnitPrice
 FROM products
 WHERE UnitPrice BETWEEN 10 and 20;
 -- Using Null Functions--
 SELECT OrderID, CustomerID, ShipRegion
 FROM orders
 WHERE ShipRegion Is NULL;
 SELECT LastName, FirstName, Region
 FROM employees
 WHERE Region IS NOT NULL;
 SELECT CompanyName
 FROM Customers
 WHERE CompanyName LIKE 'A%';
 -- Using Year and Month Functions--
 SELECT OrderID, CustomerID, OrderDate
 FROM orders
 WHERE OrderDate = '1997-01-01';
 SELECT OrderID, OrderDate
 FROM orders
 WHERE YEAR(OrderDate) = '1997' AND MONTH(OrderDate) = '6';
 -- using ascending and descending functions--
 SELECT ProductName, UnitPrice
 FROM products
 ORDER BY UnitPrice; 
 SELECT CompanyName, City, Country
 FROM customers
 ORDER BY Country ASC, CompanyName ASC;
 -- using limit function--
 SELECT ProductName, UnitPrice
 FROM products
 ORDER BY UnitPrice DESC 
 LIMIT 5;
 -- first number tells how many rows to skip while second one tells how many rows to have--
 SELECT ProductName, UnitPrice
 FROM products
 ORDER BY UnitPrice DESC
 LIMIT 5, 5;
 SELECT ProductName, UnitPrice AS 'Original Price', UnitPrice*0.90 AS '10% Disount Price'
 FROM products
 ORDER BY ProductName ASC;
 
 
 
 
 
 
 
 


