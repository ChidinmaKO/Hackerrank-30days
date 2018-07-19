SET @dr1=0, @pr2=0, @sr3=0, @ar4=0;
SELECT MIN(Doctor), MIN(Professor), MIN(Singer), MIN(Actor)
FROM (SELECT CASE occupation WHEN 'Doctor' THEN (@dr1:=@dr1+1)
                       WHEN 'Professor' THEN (@pr2:=@pr2+1)
                       WHEN 'Singer' THEN (@sr3:=@sr3+1)
                       WHEN 'Actor' THEN (@ar4:=@ar4+1)
                       END AS rowline,
      CASE WHEN occupation = 'Doctor' THEN name END AS Doctor,
      CASE WHEN occupation = 'Professor' THEN name END AS Professor,
      CASE WHEN occupation = 'Singer' THEN name END AS Singer,
      CASE WHEN occupation = 'Actor' THEN name END AS Actor
FROM occupations
ORDER BY name) AS sub
GROUP BY rowline;
--mysql

SELECT MIN(Doctor) drow, MIN(Professor) prow, MIN(Singer) srow, MIN(Actor) arow
FROM(
    SELECT CASE WHEN occupation = 'Doctor' THEN name END AS Doctor,
           CASE WHEN occupation = 'Professor' THEN name END AS Professor,
           CASE WHEN occupation = 'Singer' THEN name END AS Singer,
           CASE WHEN occupation = 'Actor' THEN name END AS Actor,
           RANK()OVER(PARTITION BY occupation ORDER BY name) AS rowline
    FROM occupations) sub_query
GROUP BY rowline
ORDER BY drow, prow, srow, arow;
--oracle

/*
    Here, I learnt about how to PIVOT tables. I also learnt about how to get non-null values after the GROUP BY clause... Using MAX()/MIN().
    Researching about the above, I understood how to normalize data and the different normal forms such as:
    1. First normal form
    2. Second normal form
    3. Third normal form
    4. Boyce and Codd Normal Form (BCNF)
    5. Fourth normal form
*/