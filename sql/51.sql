SELECT (CASE g.grade >= 8 WHEN TRUE THEN s.name ELSE NULL END), g.grade, s.marks
FROM students s
JOIN grades g
ON s.marks
BETWEEN g.min_mark AND g.max_mark
ORDER BY g.grade DESC, s.name, s.marks;
--mysql

SELECT CASE WHEN grade >= 8 THEN name WHEN grade < 8 THEN 'NULL' END AS name, grade, marks
FROM students , grades 
WHERE marks BETWEEN min_mark AND max_mark
ORDER BY grade DESC, name, marks;
--oracle