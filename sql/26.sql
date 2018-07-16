SELECT CASE 
    WHEN A + B > C AND A + C > B AND B + C > A THEN CASE 
        WHEN A = B AND B = C THEN 'Equilateral' 
        WHEN A = B OR A = C OR B = C THEN "Isosceles" 
        WHEN A != B OR A != C OR B != C THEN "Scalene" 
        END 
    ELSE "Not A Triangle" 
    END 
FROM triangles;

--mysql

SELECT 
    CASE 
        WHEN (A + B) <= C OR (B + C) <= A OR (C + A) <= B THEN 'Not A Triangle'
        WHEN A = B AND B = C THEN 'Equilateral' 
        WHEN A = B OR B = C OR A = C THEN 'Isosceles' 
        ELSE 'Scalene' 
    END 
FROM triangles;

-- oracle & Mysql
-- this was my first time of handling so many case statements!