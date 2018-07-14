SELECT SUM(ci.population) city_population
FROM city ci
JOIN country co
ON co.code = ci.countrycode
WHERE continent = 'Asia';
--mysql & oracle