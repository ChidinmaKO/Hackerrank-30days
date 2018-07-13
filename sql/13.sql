SELECT DISTINCT city FROM station WHERE REGEXP_LIKE (LOWER(city), ('[aeiou]$'));
-- oracle solution

SELECT DISTINCT city FROM station WHERE city REGEXP ('[aeiou]$');
-- mysql solution