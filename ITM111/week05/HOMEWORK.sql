-- W05 Assignment: Joining and Summarizing Data

-- 1
USE v_art;

SELECT artfile
FROM artwork
WHERE period = 'impressionism';

-- 2
SELECT artfile
FROM keyword k
	JOIN artwork_keyword ka ON  k.keyword_id = ka.keyword_id
	JOIN artwork a ON ka.artwork_id = a.artwork_id

WHERE keyword LIKE '%flower%';

-- 3

SELECT fname, lname, title
FROM artist a
	LEFT JOIN artwork ar ON a.artist_id = ar.artist_id;
  
  
-- Magazine Database
USE magazine;

-- 4
SELECT magazineName, subscriberLastName, subscriberFirstName
FROM subscriber s
	JOIN subscription sb ON s.subscriberKey = sb.subscriberKey
    JOIN magazine m ON sb.magazinekey = m.magazinekey
ORDER BY magazineName;

-- 5 
SELECT magazineName
FROM subscriber s
	JOIN subscription sb ON s.subscriberKey = sb.subscriberKey
    JOIN magazine m ON sb.magazinekey = m.magazinekey
WHERE subscriberFirstName = 'Samantha' AND subscriberLastName = 'Sanders ';


-- Employee Database
USE employees;

-- 6
SELECT first_name, 	last_name
FROM employees
ORDER BY last_name 
LIMIT 5;

-- 7

SELECT first_name, 	last_name, dept_name, salary, s.from_date
FROM employees e
	JOIN dept_manager d ON e.emp_no = d.emp_no
    JOIN salaries s ON d.emp_no = s.emp_no
    JOIN departments dp ON d.dept_no = dp.dept_no
WHERE first_name = 'Berni' AND last_name = 'Genin'
ORDER BY from_date DESC
LIMIT 5;



-- STEP 2: Summary Queries


-- bike database
USE bike;

-- 8
SELECT ROUND(AVG(quantity)) as 'Stock Average'
FROM stock;

-- 9
SELECT product_name
FROM product p
	JOIN stock s ON p.product_id = s.product_id
    JOIN store st ON s.store_id = st.store_id
WHERE quantity = 0
ORDER BY product_name;

-- 10

SELECT category_name AS category_name, SUM(quantity) AS instock
FROM product p
	JOIN category c ON p.category_id = c.category_id
	JOIN stock s ON p.product_id = s.product_id
    JOIN store st ON s.store_id = st.store_id
WHERE st.store_id = 2
GROUP BY category_name
ORDER BY instock;



-- EMPLOYEE DATABASE

USE employees;

-- 11
SELECT COUNT(emp_no) AS 'Number of Employees'
FROM employees;

-- 12
SELECT dept_name, ROUND(AVG(salary),2) AS average_salary
FROM departments d
	JOIN dept_emp de ON d.dept_no = de.dept_no
    JOIN employees e ON de.emp_no = e.emp_no
    JOIN salaries s ON e.emp_no = s.emp_no
GROUP BY dept_name;


-- 13

SELECT dept_name, COUNT(e.emp_no) AS 'Females'
FROM departments d
	JOIN dept_emp de ON d.dept_no = de.dept_no
    JOIN employees e ON de.emp_no = e.emp_no
    JOIN salaries s ON e.emp_no = s.emp_no
WHERE gender = 'F'
GROUP BY dept_name
ORDER BY dept_Name;
