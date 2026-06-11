USE v_art;

SELECT  title 
FROM artwork 
	JOIN artist
    on artwork.artist_id = artist.artist_id
WHERE lname = 'da Vinci';


SELECT * from artwork;



USE bike;

SELECT * FROM category;

SELECT * FROM product;

SELECT product_name, category_name, brand_name, list_price
FROM product p
	JOIN category c
    ON p.category_id = c.category_id
    JOIN brand b
    ON p.brand_id = b.brand_id
WHERE category_name = 'Children Bicycles';
    
SELECT * FROM brand;


SELECT first_name, last_name, store_name
from staff sf
	JOIN store st
    ON sf.store_id = st.store_id
WHERE store_name = 'rowlett Bikes';

USE v_art;

SELECT title
FROM artwork a
	JOIN artwork_keyword ak
    ON a.artwork_id = ak.artwork_id
    JOIN keyword k
    ON ak.keyword_id = k.keyword_id
WHERE keyword = 'water';


USE employees;

SELECT first_name AS 'Name', last_name AS 'Last Name', dept_name AS 'Deppartment', salary, s.from_date
FROM employees e
	JOIN dept_emp d
    ON e.emp_no = d.emp_no
    JOIN departments dept
    ON d.dept_no = dept.dept_no
    JOIN salaries s
    ON e.emp_no = s.emp_no
WHERE s.from_date > '200-12-31';

USE world;
SELECT * FROM country; 

SELECT ci.name,  co.name
FROM city ci
	JOIN country co
    ON code = countrycode;

USE bike;

SELECT first_name, last_name, p.product_name, co.order_date
FROM customer c
	JOIN cust_order co
    ON c.customer_id = co.customer_id
    JOIN cust_order_item coTra
    ON Cotra.cust_order_id = co.cust_order_id
    JOIN product p
    ON coTra.product_id = p.product_id
WHERE last_name = 'baldwin';




