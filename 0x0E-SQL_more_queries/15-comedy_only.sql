-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title
SELECT title
FROM tv_shows ts
INNER JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
INNER JOIN tv_genres tg
ON tg.id = tsg.genre_id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
