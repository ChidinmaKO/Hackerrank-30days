SELECT short_sub.c, l
FROM (SELECT city c, LENGTH(city) l FROM station ORDER BY l, c) short_sub
WHERE ROWNUM = 1;


SELECT long_sub.c, l
FROM (SELECT city c, LENGTH(city) l FROM station ORDER BY l DESC, c) long_sub
WHERE ROWNUM = 1;

-- oracle

SELECT city, CHAR_LENGTH(city) 
FROM station ORDER BY 2 ASC, 1 
LIMIT 1; 

SELECT city, CHAR_LENGTH(city) 
FROM station 
ORDER BY 2 DESC, 1 
LIMIT 1;
--mysql

--I learnt from this challenge that mysql uses the LIMIT clause while oracle uses ROWNUM.