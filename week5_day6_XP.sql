--SELECT name from language AS languages;
/*SELECT 
    film.title AS film_title, 
    film.description, 
    language.name AS language_name
FROM 
    film
JOIN 
    language ON film.language_id = language.language_id;
*/
/*SELECT 
    film.title AS film_title, 
    film.description, 
    language.name AS language_name
FROM 
    language
LEFT JOIN 
    film ON film.language_id = language.language_id;
*/

/*CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);


INSERT INTO new_film (name) VALUES ('May December');
INSERT INTO new_film (name) VALUES ('Lady in the Lake');
INSERT INTO new_film (name) VALUES ('Interstellar');
*/
-- Create customer_review table
/*CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255) NOT NULL,
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
*/

/*INSERT INTO customer_review (film_id, language_id, title, score, review_text) 
VALUES 
    ((SELECT id FROM new_film WHERE name = 'May December'), (SELECT language_id FROM language WHERE name = 'English'), 'Intriguing Drama', 8, 'A captivating story with deep character exploration and powerful performances.'),
    ((SELECT id FROM new_film WHERE name = 'Lady in the Lake'), (SELECT language_id FROM language WHERE name = 'English'), 'Mystery Thriller', 9, 'A suspenseful and engaging mystery with twists and turns that keep you hooked.');
*/
-- Delete a film from the new_film table
--DELETE FROM new_film WHERE name = 'May December';
--Exercise 2:
-- Update the language of "Inception" to French
/*UPDATE film
SET language_id = 5
WHERE title = 'Inception';

-- Update the language of "The Matrix" to German
UPDATE film
SET language_id = 6
WHERE title = 'Interstellar';
*/
--DROP TABLE customer_review;
/*SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;
*/
/*SELECT 
    film.title, 
    film.rental_rate
FROM 
    rental
JOIN 
    inventory ON rental.inventory_id = inventory.inventory_id
JOIN 
    film ON inventory.film_id = film.film_id
WHERE 
    rental.return_date IS NULL
ORDER BY 
    film.rental_rate DESC
LIMIT 30;
*/
--1st film:
/*SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.description ILIKE '%sumo%' AND a.first_name = 'Penelope' AND a.last_name = 'Monroe';
*/
--2nd film:
/*SELECT title
FROM film
WHERE length < 60 AND rating = 'R' AND description ILIKE '%documentary%';
*/
-- 3rdfilm:
/*SELECT f.title
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND f.rental_rate > 4.00
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';
*/
SELECT f.title
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;


