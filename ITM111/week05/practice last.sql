USE v_art;

SELECT COUNT(country), country
FROM artist
WHERE country = 'France';


USE bike;

select SUM(list_price), MAX(list_price), MIN(list_price)
FROM product;

select model_year, FORMAT(AVG(DISTINCT list_price),2)
FROM product
WHERE list_price > 2800
GROUP BY model_year WITH ROLLUP
HAVING AVG(list_price) > 300;

-- Average of each brand list price with no 2016 and only averages over $2000
SELECT brand_name, AVG(list_price)
FROM product p
	JOIN brand b
    ON p.brand_id = b.brand_id
WHERE model_year > '2016'
GROUP BY brand_name with ROLLUP
HAVING AVG(list_price) > 2000;


USE magazine;



