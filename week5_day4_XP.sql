--SELECT * FROM customer
--SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;
--SELECT DISTINCT create_date FROM customer;
--SELECT * FROM customer ORDER BY first_name DESC;
/*SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;
*/
/*SELECT address, phone
FROM address
WHERE district = 'Texas';
*/
--SELECT * FROM film WHERE film_id IN (15, 150);
/*SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = "Love actually";
*/
/*SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE 'Lo%';  
*/
/*SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 10;
*/
/*SELECT cu.first_name, cu.last_name, pa.amount, pa.payment_date
FROM customer cu
JOIN payment pa ON cu.customer_id = pa.customer_id
ORDER BY cu.customer_id;
*/
/*SELECT * FROM film
LEFT JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.film_id IS NULL;
*/
SELECT ci.city, co.country
FROM city ci
JOIN country co ON ci.country_id = co.country_id;

