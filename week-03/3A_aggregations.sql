-- Sha'Rya Weaver
USE northwind;

-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to find the name of the product that has that price.
    -- PART 1--
SELECT MIN(UnitPrice) AS CheapestPrice
FROM products;  -- Price of the cheapest item is 2.5000--
   -- PART 2--
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = ( SELECT MIN(UnitPrice) FROM products);   -- Name of the product name is Geitost--


-- 2. Write a query to find the average price of all items that Northwind sells. 
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help using the ROUND function to round the average price to the nearest cent.)

-- PART 1--
SELECT AVG(UnitPrice)
FROM products;

-- PART 2 on my own--
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM Products;  -- UnitPrice rounded up is 28.87--

-- Part 2 using ChatGPT--
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM Products;  -- UnitPrice rounded to the nearest cent is 28.87--


-- 3. Write a query to find the price of the most expensive item that Northwind sells.
-- Then write a second query to find the name of the product with that price, plus the name of the supplier for that product.
   -- Part 1--
SELECT MAX(UnitPrice) AS MostExpensive
FROM products;
   -- Part 2--
SELECT p.UnitPrice, p.ProductName, s.CompanyName
   FROM products p  
INNER JOIN suppliers s
   ON p.SupplierID = s.SupplierID
WHERE UnitPrice = (SELECT MAX(p.UnitPrice) FROM products)
GROUP BY p.ProductName, s.CompanyName;

-- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).

SELECT EmployeeID, LastName, FirstName, ROUND(SUM(Salary), 2) AS MonthlySalary
FROM employees
GROUP BY EmployeeID;

-- 5. Write a query to identify the highest salary and the lowest salary amounts which any employee makes. (Just the amounts, not the specific employees!)

SELECT MAX(salary), MIN(salary)
FROM employees;  -- Max = 3119.15 and Min = 1744.21--

-- 6. Write a query to find the name and supplier ID of each supplier and the number of items they supply. Hint: Join is your friend here.

SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID) AS 'ItemCount'
FROM suppliers s
INNER JOIN products p 
		ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
ORDER BY ItemCount DESC;

-- 7. Write a query to find the list of all category names and the average price for items in each category.

SELECT c.CategoryName, ROUND(AVG(p.Unitprice), 2) AS AveragePrice
FROM categories c 
INNER JOIN products p 
        ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, 
-- what is the name of each supplier and the number of items they supply.

SELECT COUNT(p.ProductID) AS 'NumberOfItems', s.CompanyName
FROM products p 
INNER JOIN suppliers s  
		ON s.SupplierId = p.SupplierID
GROUP BY s.CompanyName HAVING COUNT(p.ProductID) >= 5
ORDER BY NumberOfItems;

-- 9. Write a query to list products currently in inventory by the product id, product name, and inventory value (calculated by multiplying unit price by the number of units on hand). 
-- Sort the results in descending order by value. If two or more have the same value, order by product name. If a product is not in stock, leave it off the list.

SELECT ProductID, ProductName, ROUND((UnitPrice*UnitsInStock), 2) AS InventoryValue
FROM products
WHERE UnitsInStock > 0 ORDER BY ProductName, InventoryValue DESC;