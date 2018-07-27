SELECT f.x, f.y
FROM functions f
WHERE f.x = f.y 
GROUP BY f.x, f.y
HAVING COUNT(*) > 1
UNION
SELECT f.x, f.y
FROM functions f, functions f1
WHERE EXISTS (
    SELECT x, y
    FROM functions
    WHERE f.x= y AND f.y = x AND f.x < x)
ORDER BY x;


--OR 

SELECT f.x, f.y
FROM functions f
WHERE f.x = f.y 
GROUP BY f.x, f.y
HAVING COUNT(*) > 1
UNION
SELECT f.x, f.y
FROM functions f, functions f1
WHERE f.x != f.y AND f.x = f1.y AND f.y = f1.x AND f.x < f1.x
ORDER BY x;

--mysql & oracle