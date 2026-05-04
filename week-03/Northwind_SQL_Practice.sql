Use northwind;
/* Question 1*/ 
SELECT CategoryID, CategoryName, Description
FROM categories;

-- Question 2--
SELECT ProductID, ProductName, Discontinued
FROM products


-- Question 3--



-- Question 4--



-- Question 5--



/* Question 6 */

SELECT OrderID COUNT(OrderID) AS TotalOrders 
FROM orders;