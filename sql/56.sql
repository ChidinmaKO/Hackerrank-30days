SELECT s.name
FROM students s
JOIN friends f
ON s.id = f.id
JOIN packages sp
ON f.id = sp.id
JOIN packages fp
ON f.friend_id = fp.id 
WHERE sp.salary <  fp.salary
ORDER BY fp.salary;
--mysql & oracle