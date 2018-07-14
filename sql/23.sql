SELECT co.continent, FLOOR(AVG(ci.population)) AS avg_pop
FROM city ci
JOIN country co
ON co.code = ci.countrycode
GROUP BY 1;
--mysql

SELECT country.continent, FLOOR(AVG(city.population)) AS avg_pop
FROM city
JOIN country
ON country.code = city.countrycode
GROUP BY country.continent;
--oracle

-- here I noticed that using aliases doesn't quite work well with oracle.