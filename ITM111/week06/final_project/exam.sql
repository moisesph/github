USE world;


SELECT name, SUM(population) AS 'population'
FROM country 
WHERE population <5000000
GROUP BY name
ORDER BY population DESC
LIMIt 5;



SELECT DISTINCT language
FROM country c
JOIN city ci ON c.code = ci.countrycode
JOIN countryLanguage cl ON c.code = cl.countrycode
ORDER BY language;



SELECT  continent, count(continent) AS 'counter'
FROM country c
JOIN city ci ON c.code = ci.countrycode
JOIN countryLanguage cl ON c.code = cl.countrycode
GROUP BY continent
 ;
 
SELECT DISTINCT c.name
FROM country c
JOIN city ci ON c.code = ci.countrycode
JOIN countryLanguage cl ON c.code = cl.countrycode
where c.continent = 'North America'
 ;
 
SELECT DISTINCT c.name, AVG(c.population) AS population
FROM country c
JOIN city ci ON c.code = ci.countrycode
JOIN countryLanguage cl ON c.code = cl.countrycode
WHERE c.name = 'liberia'
GROUP by name
;