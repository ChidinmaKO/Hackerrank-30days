SELECT DISTINCT city FROM station WHERE REGEXP_LIKE (LOWER(city), '^[^aeiou].*');
SELECT DISTINCT city FROM station WHERE REGEXP_LIKE (LOWER(city), '^[^aeiou]');
--oracle

SELECT DISTINCT city FROM station WHERE city REGEXP ('^[^aeiou].*');
SELECT DISTINCT city FROM station WHERE city RLIKE ('^[^aeiou].*');
--mysql