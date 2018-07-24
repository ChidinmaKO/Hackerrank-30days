SELECT sq.hacker_id, h.name, SUM(sq.max_score) total_score
FROM(
SELECT MAX(score) max_score, hacker_id, challenge_id
FROM submissions
GROUP BY hacker_id, challenge_id) sq
JOIN hackers h
ON h.hacker_id = sq.hacker_id
GROUP BY sq.hacker_id, h.name
HAVING SUM(sq.max_score) > 0
ORDER BY SUM(sq.max_score) DESC, hacker_id;
--oracle

SELECT sq.hacker_id, h.name, SUM(sq.max_score) total_score
FROM(
SELECT MAX(score) max_score, hacker_id, challenge_id
FROM submissions
GROUP BY hacker_id, challenge_id) sq
JOIN hackers h
ON h.hacker_id = sq.hacker_id
GROUP BY 1,2
HAVING total_score > 0
ORDER BY 3 DESC, 1;
--oracle

--both solutions are alike but oracle doesn't recognize some aliases (see the "having and order by clause");