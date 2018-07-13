/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT DISTINCT city 
FROM station 
WHERE MOD(id, 2) = 0;

-- this is where I learnt about how to search for even/odd numbers
-- Using (id % 2) = 0.
-- MOD(id, 2) = 0 works  on Oracle & Mysql platforms

SELECT DISTINCT city 
FROM station 
WHERE (id % 2) = 0;