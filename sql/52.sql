SELECT id, age, s.coins_needed, s.power
FROM(
    SELECT power, code, MIN(coins_needed) AS coins_needed
    FROM wands
    GROUP BY code, power) s
JOIN wands w
ON s.code = w.code AND s.power = w.power AND s.coins_needed = w.coins_needed
JOIN wands_property wp
ON wp.code = s.code
WHERE wp.is_evil = 0
ORDER BY s.power DESC, age DESC;
--mysql & oracle