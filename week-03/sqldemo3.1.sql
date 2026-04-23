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
 
 USE northwind;
 -- EXAMPLE 1
 SELECT o.OrderID,
 c.CompanyName AS 'Customer',
 o.OrderDate
 FROM Orders o
 JOIN Customers c ON o.CustomerID = c.CustomerID
 ORDER BY o.OrderDate DESC
 LIMIT 5;

-- EXAMPLE 2
SELECT OrderID, CompanyName, OrderDate
FROM Orders
JOIN Customers USING (CustomerID)
LIMIT 5;

-- EXAMPLE 3
SELECT p.ProductName, c.CategoryName, p.UnitPrice
FROM Products p
INNER JOIN Categories c ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName
LIMIT 6;
-- Another way
SELECT p.ProductName, c.CategoryName, p.UnitPrice
FROM products p
INNER JOIN Categories c USING (CategoryID)
ORDER BY c.CategoryName, p.ProductName
LIMIT 6;

-- EXAMPLE 5
-- CUSTOMERS WITH ZERO ORDERS WILL SHOW 0 IN ORDER COUNT
SELECT c.CompanyName, COUNT(o.OrderID) AS 'Order Count'
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CompanyName
ORDER BY 'Order Count' ASC
LIMIT 5;

 -- EXAMPLE 1: Total Number of Orders--
 -- Find out how many orders are recordered in the Orders table in total--
 USE northwind;
 SELECT COUNT(*) AS 'Total Orders'
 FROM orders;
 SELECT COUNT(OrderID) AS 'Total Orders'
 FROM orders;
 
 -- EXAMPLE 2 Total Freight Charged--
 -- 
 SELECT SUM(Freight) AS 'Total Freight', 
 AVG(Freight) AS 'Average Freight',
 MIN(Freight) AS 'Minmum Freight',
 MAX(Freight) AS 'Maximum Freight'
 FROM orders;
 
 
 
 
 
 
 


