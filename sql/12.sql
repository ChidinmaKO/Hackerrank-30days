SELECT DISTINCT city FROM station WHERE REGEXP_LIKE (LOWER(city),'^[aeiou].*');
SELECT DISTINCT city FROM station WHERE REGEXP_LIKE (LOWER(city), '^[aeiou]');
-- oracle

-- here I figured out the difference between RLIKE, LIKE, REGEXP_LIKE

SELECT DISTINCT city FROM station WHERE city REGEXP ('^[aeiou].*');
SELECT DISTINCT city FROM station WHERE city RLIKE ('^[aeiou].*');
-- mysql
