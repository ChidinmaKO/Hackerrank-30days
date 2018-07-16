SELECT CONCAT(name, '(', LEFT(occupation, 1), ')')
FROM occupations
ORDER BY name;

SELECT CONCAT('There are a total of ', COUNT(occupation), ' ', LOWER(occupation), 's.')
FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation), occupation;

-- OR 

SELECT CONCAT(name, '(', SUBSTR(occupation, 1,1), ')')
FROM occupations
ORDER BY name;

SELECT CONCAT('There are a total of ', COUNT(occupation), ' ', LOWER(occupation), 's.')
FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation), occupation;

--mysql

SELECT name || '(' || SUBSTR(occupation, 1,1) || ')'
FROM occupations
ORDER BY name;

SELECT 'There are a total of ' || COUNT(occupation) || ' ' || LOWER(occupation) || 's.'
FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation), occupation;
-- oracle