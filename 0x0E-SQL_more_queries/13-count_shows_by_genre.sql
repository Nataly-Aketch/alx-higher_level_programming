-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column is called genre
-- Second column is called number_of_shows
-- Doesn’t display a genre that wiyhout any shows linked
-- Results are sorted in descending order by the number of shows linked
SELECT name as 'genre', COUNT(*) as 'number_of_shows'
FROM tv_genres tg
INNER JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
GROUP BY tsg.genre_id
ORDER BY number_of_shows DESC;
