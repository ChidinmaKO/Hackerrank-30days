SET @number = 21;
SELECT REPEAT('* ', @number := @number - 1)
FROM information_schema.tables 
LIMIT 20;
-- mysql
-- learnt how to declear variables (SET @number = 21;)

SELECT RPAD('*', (21-LEVEL)*2, ' *') 
FROM DUAL CONNECT BY LEVEL <= 20;
--oracle
-- it took me a while to figure out 'DUAL CONNECT BY LEVEL'