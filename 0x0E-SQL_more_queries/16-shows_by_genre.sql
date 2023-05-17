-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- displays NULL in the genre column if show doesn't have genre
-- Each record displays: tv_shows.title - tv_genres.name
-- Results are sorted in ascending order by the show title and genre name
SELECT ts.title, tg.name
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg
ON tg.id = tsg.genre_id
ORDER BY ts.title ASC, tg.name ASC;
