SELECT ROUND(SQRT(POW(MIN(lat_n) - MAX(lat_n), 2) + POW(MIN(long_w) - MAX(long_w), 2)), 4)
FROM station;
--mysql

SELECT ROUND(SQRT(POWER(MIN(lat_n) - MAX(lat_n), 2) + POWER(MIN(long_w) - MAX(long_w), 2)), 4)
FROM station;
--oracle

-- used the POWER(), POW(), SQRT() functions to calculate the euclidean distance (the straight line distance between two points √((x1 - x2)² + (y1 - y2)²))