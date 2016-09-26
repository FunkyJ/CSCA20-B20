SELECT COUNT(gender) FROM actors WHERE gender='F';
SELECT first_name, last_name FROM actors JOIN roles WHERE actor_id = id AND role='Superman';
SELECT NULL;
SELECT DISTINCT first_name, last_name, name FROM directors JOIN movies_directors JOIN movies WHERE directors.id = director_id AND movie_id = movies.id;
SELECT DISTINCT first_name, last_name, name FROM directors JOIN movies_directors JOIN movies WHERE directors.id = director_id AND movie_id = movies.id AND rank>=9.5;
SELECT DISTINCT CONCAT_WS(' ', first_name, last_name) AS Name FROM actors JOIN roles WHERE id = actor_id AND role='Herself';
SELECT year, AVG(rank) FROM movies GROUP BY year;
SELECT DISTINCT first_name, last_name, COUNT(role) AS Roles_played FROM actors JOIN roles WHERE actor_id = id AND gender='M' GROUP BY first_name, last_name HAVING count(role)>=3
SELECT DISTINCT name FROM movies JOIN movies_genres WHERE movie_id = id AND (genre='Comedy' or genre='Action');
SELECT DISTINCT name FROM movies JOIN movies_genres WHERE movie_id = id AND genre IN ('Comedy','Action');
SELECT DISTINCT name FROM movies HAVING name LIKE '%Star% %Wars%';
SELECT DISTINCT directors.first_name, directors.last_name, name, role FROM directors JOIN actors JOIN roles JOIN movies where directors.first_name = actors.first_name and directors.last_name = actors.last_name and actors.id = roles.actor_id and roles.movie_id = movies.id;
SELECT genre FROM (SELECT genre, count(genre) AS numbers FROM movies_genres GROUP BY genre ORDER BY numbers DESC limit 1) AS new;

SELECT DISTINCT name FROM movies ORDER BY rank DESC limit 25;