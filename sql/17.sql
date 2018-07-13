/*Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.*/

SELECT DISTINCT city FROM station WHERE NOT REGEXP_LIKE (LOWER(city), '^[aeiou].*[aeiou]$');
--oracle

SELECT DISTINCT CITY FROM STATION WHERE CITY NOT RLIKE '^[aeiou].*[aeiou]$';
--mysql