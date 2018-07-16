SELECT *
FROM(
SELECT (months * salary) AS total_salary, COUNT(*) 
FROM employee
GROUP BY (months * salary)
ORDER BY (months * salary) DESC)
WHERE ROWNUM = 1;
-- oracle

SELECT (months * salary) AS total_salary, COUNT(*)
FROM employee
GROUP BY 1
ORDER BY 1 DESC
LIMIT 1;
-- mysql