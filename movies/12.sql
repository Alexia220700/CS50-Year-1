SELECT movies.title
FROM movies
WHERE EXISTS (SELECT 1 FROM stars JOIN people ON people.id = stars.person_id
    WHERE stars.movie_id = movies.id AND people.name = "Bradley Cooper")
AND EXISTS (SELECT 1 FROM stars JOIN people ON people.id = stars.person_id
    WHERE stars.movie_id = movies.id AND people.name = "Jennifer Lawrence");

