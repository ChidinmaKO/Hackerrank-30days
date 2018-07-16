SET @number = 0;
SELECT REPEAT('* ', @number := @number + 1)
FROM information_schema.tables
LIMIT 20;

--mysql

SELECT RPAD('*', (2 * LEVEL) - 1, ' *') 
FROM DUAL CONNECT BY LEVEL <= 20;
--oracle