SET @rowIndex := -1;
SELECT ROUND(AVG(sub.lat_n), 4) median
FROM(
    SELECT @rowIndex := @rowIndex + 1 AS row_index, s.lat_n
    FROM station s
    ORDER BY s.lat_n) sub
WHERE sub.row_index IN (FLOOR(@rowIndex/2), CEIL(@rowIndex/2));
--mysql 

SELECT ROUND(MEDIAN(lat_n), 4) median
FROM station s;
--oracle