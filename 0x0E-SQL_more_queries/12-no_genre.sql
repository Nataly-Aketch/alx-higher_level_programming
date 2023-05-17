-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT s.title, g.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres g
ON s.id = g.show_id
WHERE g.show_id is NULL
ORDER BY title ASC, genre_id ASC;
