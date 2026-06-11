

-- PART 1
USE v_art;

#1
INSERT INTO artist VALUES
(NULL, 'Johannes', NULL, 'Vermeer', 1632, 1674, 'Netherlands',  'n');

#2
SELECT fname, lname, dob, country
FROM artist
ORDER BY lname;

#3
UPDATE artist
SET dod = 1674
WHERE lname = 'Vermeer';

#4
DELETE FROM artist
WHERE lname = 'vermeer';


-- PART 2
USE bike;

#5
SELECT first_name, last_name, phone
FROM customer
WHERE city = 'Houston';


#6
SELECT product_name, list_price, list_price - 500 as 'Discount Price'
FROM product
WHERE list_price >= 5000.00
ORDER BY list_price DESC;

#7
SELECT first_name, last_name, email
FROM staff
WHERE store_id <> 1;

#8
SELECT product_name, model_year, list_price
FROM product
WHERE product_name LIKE '%spider%';

#9
SELECT product_name, list_price
FROM product
WHERE list_price >= 500 AND list_price <=550 
ORDER BY list_price;

#10
SELECT first_name, last_name, phone, street, city, state, zip_code
FROM customer
WHERE phone IS NOT NULL and city LIKE '%ach%' OR phone IS NOT NULL AND city LIKE '%och%' OR last_name = 'William'
LIMIT 5;

#11  
SELECT REPLACE(REPLACE (product_name, 'Surly', ''), 'Trek', '') AS Model  
FROM product
WHERE product_name LIKE '%Trek%' OR  product_name LIKE '%Surly%'
ORDER BY product_id
LIMIT 10;

#12
SELECT product_name, CONCAT('$', ROUND(list_price / 3, 2)) as 'One of 3 payments' -- 3 because is of 3 payments
FROM product
WHERE model_year = 2025;


-- PART 3
USE magazine;

#13
SELECT magazineName, ROUND(magazinePrice - (magazinePrice * 0.03),2) AS '3% off'
FROM magazine;

#14
SELECT subscriberKey, TIMESTAMPDIFF(YEAR, subscriptionStartDate, '2020-12-20') as 'Years since subscription'
FROM subscription;

#15

SELECT DATE_FORMAT(subscriptionstartdate,'%m-%d-%Y'), subscriptionlength, DATE_FORMAT(DATE_ADD(subscriptionstartdate, INTERVAL subscriptionlength YEAR), '%M-%d-%Y' ) AS 'subscription end'
FROM subscription;