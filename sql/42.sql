SELECT ROUND((long_w), 4)
FROM station
WHERE lat_n < 137.2345
ORDER BY lat_n DESC
LIMIT 1;
--mysql

SELECT ROUND((long_w), 4)
FROM(
    SELECT long_w
    FROM station
    WHERE lat_n < 137.2345
    ORDER BY lat_n DESC)
WHERE ROWNUM = 1;
--oracle