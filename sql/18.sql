/*Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.*/

SELECT DISTINCT city FROM station WHERE REGEXP_LIKE (LOWER(city), '^[^aeiou].*[^aeiou]$');
--oracle

SELECT DISTINCT CITY FROM STATION WHERE CITY RLIKE '^[^aeiou].*[^aeiou]$';
--mysql