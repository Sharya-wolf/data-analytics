USE Sakila;

-- Example 1
SELECT 
  film.title AS Film_Title,
  category.name AS Category_Name,
  film.rental_rate AS Rental_Rate
FROM film
  INNER JOIN film_category
    ON film.film_id = film_category.film_id
  INNER JOIN category
    ON film_category.category_id = category.category_id
ORDER BY film.rental_rate 
LIMIT 20;

-- Example 2
SELECT film.title, 
rental.rental_date, 
rental.return_date
FROM film
LEFT OUTER JOIN inventory ON film.film_id = inventory.film_id
LEFT OUTER JOIN rental 
ON inventory.inventory_id = rental.inventory_id
ORDER BY film.title;

-- Example 3
SELECT film.film_id, film.title, category.name AS category_name
FROM category
RIGHT JOIN film_category
ON category.category_id = film_category.category_id
RIGHT JOIN film ON film_category.film_id = film.film_id;

-- Example 4
SELECT
  c.customer_id,
  c.first_name,
  c.last_name,
  r.rental_id,
  r.rental_date
FROM customer c
  LEFT JOIN rental r
    ON c.customer_id = r.customer_id
UNION
SELECT
  c.customer_id,
  c.first_name,
  c.last_name,
  r.rental_id,
  r.rental_date
FROM customer c
  RIGHT JOIN rental r
    ON c.customer_id = r.customer_id;
    
-- Example 5
SELECT
  actor.actor_id,
  actor.first_name,
  actor.last_name,
  film.title
FROM actor
  CROSS JOIN film;
  

