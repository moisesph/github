USE v_art;

select * FROM artwork;

SELECT title,period,artyear
FROM artwork
WHERE artyear > 1800 AND artyear < 1900;
-- Another way to get a filter with range
SELECT title,period,artyear
FROM artwork
WHERE artyear BETWEEN 1800 AND 1900;

SELECT title, period
FROM artwork
WHERE period IN ('Modern','Baroque', 'Impressionism');

SELECT title, period
FROM artwork
WHERE period LIKE '_ost-impression%';

SELECT title, period
FROM artwork
WHERE title REGEXP 'the|in|on';

SELECT * FROM artist;

select fname as  First,mname as Middle,lname as Last
FROM artist
WHERE mname IS NULL
Order BY Middle;


USE bike;

SELECT * FROM product;

SELECT product_name,model_year, list_price + 100 AS 'Marked_up', list_price
FROM product
WHERE list_price + 100 > 1000
ORDER By marked_up;

Select product_name, model_year
from product
Where (product_name LIKE 'Trek%' OR product_name LIKE 'Surly%') AND model_year <> 2016;
