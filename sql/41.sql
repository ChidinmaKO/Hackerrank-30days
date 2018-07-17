SELECT TRUNC(MAX(lat_n), 4)
FROM station
WHERE lat_n < 137.2345;
-- oracle

SELECT TRUNCATE(MAX(lat_n), 4)
FROM station
WHERE lat_n < 137.2345;
--mysql