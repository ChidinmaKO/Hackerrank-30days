SELECT ROUND((long_w), 4)
FROM(
    SELECT long_w
    FROM station
    WHERE lat_n > 38.7780
    ORDER BY lat_n)
WHERE ROWNUM = 1;
-- oracle

SELECT ROUND((long_w), 4)
FROM station
WHERE lat_n > 38.7780
ORDER BY lat_n
LIMIT 1;
--mysql