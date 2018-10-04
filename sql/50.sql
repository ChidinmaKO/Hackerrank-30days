SELECT c.hacker_id, h.name, COUNT(c.challenge_id) AS total_c
FROM hackers h
JOIN challenges c
ON h.hacker_id = c.hacker_id
GROUP BY 1, 2
HAVING total_c = (
    SELECT COUNT(c2.challenge_id) AS c2_count
    FROM challenges AS c2
    GROUP BY c2.hacker_id
    ORDER BY c2_count DESC
    LIMIT 1) 
OR
total_c NOT IN (
    SELECT COUNT(c3.challenge_id) AS c3_count
    FROM challenges AS c3
    GROUP BY c3.hacker_id
    HAVING c3.hacker_id != c.hacker_id
)
ORDER BY 3 DESC, h.hacker_id;
--mysql