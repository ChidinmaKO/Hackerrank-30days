SELECT DISTINCT city FROM station WHERE city REGEXP ('[^aeiou]$');
--mysql

SELECT DISTINCT city FROM station WHERE REGEXP_LIKE (LOWER(city), ('[^aeiou]$'));
--oracle