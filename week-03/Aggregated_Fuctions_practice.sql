-- Aggregated Functions
-- Sha'Rya Weaver
USE sakila;

-- Count--
-- How many films belong to the "Action" category--
SELECT COUNT(*)
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action';

-- Using Count(Distinct column_name) to count unique entries--
-- What is the number of unique categories in the category tabel--
SELECT COUNT(DISTINCT name)
FROM category;

-- Summing data with SUM--
-- What is the totel amount of rentals from the rental table:--
SELECT SUM(amount)
FROM payment;

-- to calculate the total payment amount per customer, you can use the following query.--
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id;

-- What is the total payment per customer from highest to lowest? What is the number one film--
SELECT customer_id, rental_id, last_update, SUM(amount)
FROM payment
GROUP BY customer_id, rental_id, last_update 
ORDER BY SUM(amount) DESC;
SELECT last_update, title, film_id
FROM film
ORDER BY last_update DESC;
SELECT film_id, last_update, inventory_id
FROM inventory
ORDER BY last_update DESC;

-- To calculate both average and total payment amounts--
SELECT AVG(amount), SUM(amount)
FROM payment;

-- FINDING AVERAGES WITH AVG--
-- To calculate the average film length from the film table in the sakila database--
SELECT AVG(length)
FROM film;
-- Decimals and precision--
SELECT ROUND(AVG(amount), 2)
FROM payment;



