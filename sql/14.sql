SELECT DISTINCT city FROM station WHERE REGEXP_LIKE (LOWER(city), '^[aeiou].*[aeiou]$');
--oracle

SELECT DISTINCT city FROM station WHERE city REGEXP ('^[aeiou].*[aeiou]$');
-- mysql