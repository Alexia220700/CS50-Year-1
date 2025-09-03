--using var average_rating to make output more readable
SELECT AVG(ratings.rating) AS average_rating
FROM movies
--make use of data stored in two tables
JOIN ratings ON movies.id = ratings.movie_id
WHERE movies.year = 2012;
