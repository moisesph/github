-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema university
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema university
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `university` DEFAULT CHARACTER SET utf8 ;
USE `university` ;

-- -----------------------------------------------------
-- Table `university`.`student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university`.`student` (
  `student_id` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `gender` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(4) NULL,
  `birthdate` DATE NULL,
  PRIMARY KEY (`student_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`college`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university`.`college` (
  `college_id` INT NOT NULL,
  `college` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`college_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`department`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university`.`department` (
  `department_id` INT NOT NULL,
  `department` VARCHAR(45) NOT NULL,
  `department_code` VARCHAR(45) NOT NULL,
  `college_id` INT NOT NULL,
  PRIMARY KEY (`department_id`),
  INDEX `fk_department_college_idx` (`college_id` ASC) VISIBLE,
  CONSTRAINT `fk_department_college`
    FOREIGN KEY (`college_id`)
    REFERENCES `university`.`college` (`college_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`course`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university`.`course` (
  `course_id` INT NOT NULL,
  `course_num` INT NOT NULL,
  `course_title` VARCHAR(45) NOT NULL,
  `credits` INT NOT NULL,
  `department_id` INT NOT NULL,
  PRIMARY KEY (`course_id`),
  INDEX `fk_course_department1_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `fk_course_department1`
    FOREIGN KEY (`department_id`)
    REFERENCES `university`.`department` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`faculty`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university`.`faculty` (
  `faculty_id` INT NOT NULL,
  `faculty_fname` VARCHAR(45) NOT NULL,
  `faculty_lname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`faculty_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`term`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university`.`term` (
  `term_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `year` YEAR NOT NULL,
  PRIMARY KEY (`term_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`Section`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university`.`Section` (
  `Section_id` INT NOT NULL,
  `Section` INT NOT NULL,
  `capacity` INT NOT NULL,
  `course_id` INT NOT NULL,
  `faculty_id` INT NOT NULL,
  `term_id` INT NOT NULL,
  PRIMARY KEY (`Section_id`),
  INDEX `fk_Section_course1_idx` (`course_id` ASC) VISIBLE,
  INDEX `fk_Section_faculty1_idx` (`faculty_id` ASC) VISIBLE,
  INDEX `fk_Section_term1_idx` (`term_id` ASC) VISIBLE,
  CONSTRAINT `fk_Section_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `university`.`course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Section_faculty1`
    FOREIGN KEY (`faculty_id`)
    REFERENCES `university`.`faculty` (`faculty_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Section_term1`
    FOREIGN KEY (`term_id`)
    REFERENCES `university`.`term` (`term_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`enrollment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university`.`enrollment` (
  `student_id` INT NOT NULL,
  `Section_id` INT NOT NULL,
  PRIMARY KEY (`student_id`, `Section_id`),
  INDEX `fk_student_has_Section_Section1_idx` (`Section_id` ASC) VISIBLE,
  INDEX `fk_student_has_Section_student1_idx` (`student_id` ASC) VISIBLE,
  CONSTRAINT `fk_student_has_Section_student1`
    FOREIGN KEY (`student_id`)
    REFERENCES `university`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_has_Section_Section1`
    FOREIGN KEY (`Section_id`)
    REFERENCES `university`.`Section` (`Section_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



USE university;

INSERT INTO college
VALUES (1, 'Physical Science and Engineering'),
(2, 'Business and Communication'),
(3, 'Language and Letters');

INSERT INTO department VALUES
(1, 'Computer Information Technology', 'ITM', 1),
(2, 'Economics', 'ECON', 2),
(3, 'Humanities and Philosophy', 'HUM', 3);

INSERT INTO course VALUES
(1, 111, 'Intro to Databases', 3, 1),
(2, 388, 'Econometrics', 4, 2),
(3, 150, 'Micro Economics', 3, 2),
(4, 376, 'Classical Heritage', 2, 3)
;


INSERT INTO faculty VALUES
(1, 'Marty', 'Morring'),
(2, 'Nate', 'Norris'),
(3, 'Ben', 'Barrus'),
(4, 'John', 'Jensen'),
(5, 'Bill', 'Barney')
;

INSERT INTO term VALUES
(1, 'Fall', 2019),
(2, 'Winter', 2018);



INSERT INTO section VALUES
-- id, section, capacity, course, faculty, term
(1,1, 30, 1, 1, 1),
(2,1, 50, 3, 2, 1),
(3,2, 50, 3, 2, 1),
(4,1, 35, 2, 3, 1),
(5,1, 30, 4, 4, 1),
(6,2, 30, 1, 1, 2),
(7,3, 35, 1, 5, 2),
(8,1, 50, 3, 2, 2),
(9,2, 50, 3, 2, 2),
(10,1, 30, 4, 4, 2);

INSERT INTO student VALUES
(1, 'Paul', 'Miller', 'M', 'Dallas', 'TX', '1996-02-22'),
(2, 'Katie', 'Smith', 'F', 'Provo', 'UT', '1995-07-22'),
(3, 'Kelly', 'Jones', 'F', 'Provo', 'UT', '1998-06-22'),
(4, 'Devon', 'Merrill', 'M', 'Mesa', 'AZ', '2000-07-22'),
(5, 'Mandy', 'Murdock', 'F', 'Topeka', 'KS', '1996-11-22'),
(6, 'Alece', 'Adams', 'F', 'Rigby', 'ID', '1997-05-22'),
(7, 'Bryce', 'Carlson', 'M', 'Bozeman', 'MT', '1997-11-22'),
(8, 'Preston', 'Larsen', 'M', 'Decatur', 'TN', '1996-09-22'),
(9, 'Julia', 'Madsen', 'F', 'Rexburg', 'ID', '1998-09-22'),
(10, 'Susan', 'Sorensen', 'F', 'Mesa', 'AZ', '1998-08-09');

INSERT INTO enrollment VALUES
-- student, section
(6, 7),
(7, 6),
(7,3),
(7,10),
(4,2),
(9,9),
(2,4),
(3,4),
(5,4),
(5,5),
(1,1),
(1,3),
(8,9),
(10,6);


-- 1
select first_name AS 'fname', last_name AS 'lname', DATE_FORMAT(Birthdate, '%M %d,%Y') AS 'Sept Birthdays'
FROM student
WHERE MONTH(birthdate) = 9;

-- 2
select first_name AS 'fname', last_name AS 'lname', TIMESTAMPDIFF(YEAR, birthdate, CURDATE()) AS 'YEARS', 
DATEDIFF(CURDATE(), birthdate) % 365 AS 'Years and Days', 
CONCAT(TIMESTAMPDIFF(YEAR, birthdate, CURDATE()), ' - Yrs, ', DATEDIFF(CURDATE(), birthdate) % 365, ' - Days') AS 'Years and Days'
FROM student
ORDER BY YEARS DESC
;

-- 3
select first_name AS 'fname', last_name AS 'lname'
FROM student s
JOIN enrollment e ON s.student_id = e.student_id
JOIN section se ON e.section_id = se.section_id
WHERE faculty_id = 4
;

-- 4

select faculty_fname AS 'fname', faculty_lname AS 'lname'
FROM faculty f
JOIN section se ON f.faculty_id = se.faculty_id
JOIN enrollment e ON se.section_id = e.section_id
JOIN term t ON se.term_id = t.term_id
WHERE t.term_id = 2 AND year = '2018' AND student_Id = 7
ORDER BY lname
;

-- 5
select first_name AS 'fname', last_name AS 'lname'
FROM student s
JOIN enrollment e ON s.student_id = e.student_id
JOIN section se ON e.section_id = se.section_id
JOIN course c ON se.course_id = c.course_id
JOIN term t ON se.term_id = t.term_id
WHERE t.term_id = 1 AND year = '2019'  AND se.course_id = 2
ORDER BY lname
;

-- 6

SELECT department_code AS 'department_code', course_num AS 'course_num', course_title AS 'name'
FROM department d
JOIN course c ON d.department_id = c.department_id
JOIN section s ON c.course_id = s.course_id
JOIN term t ON s.term_id = t.term_id
JOIN faculty f ON s.faculty_id = f.faculty_id
JOIN enrollment en ON s.section_id = en.section_id
JOIN student st ON en.student_id = st.student_id
WHERE st.student_id = 7
ORDER BY name;

-- 7
SELECT COUNT(*) AS Enrollment
FROM enrollment e
JOIN section s ON e.section_id = s.section_id
JOIN term t ON s.term_id = t.term_id
WHERE t.name = 'Fall' AND t.year = 2019;

-- 8
SELECT college AS colleges, COUNT(*) AS courses
FROM college c
JOIN department d ON c.college_id = d.college_id
JOIN course co ON d.department_id = co.department_id
GROUP BY colleges
ORDER BY courses DESC;

-- 9
select DISTINCT faculty_fname AS 'fname', faculty_lname AS 'lname', capacity AS TeachingCapacity
FROM student s
JOIN enrollment e ON s.student_id = e.student_id
JOIN section se ON e.section_id = se.section_id
JOIN course c ON se.course_id = c.course_id
JOIN term t ON se.term_id = t.term_id
JOIN faculty fa ON se.faculty_id = fa.faculty_id
WHERE t.name = 'Fall' AND t.year = 2019
ORDER BY TeachingCapacity
;

-- 10

select first_name AS 'fname', last_name AS 'lname', SUM(credits) AS Credits
FROM student s
JOIN enrollment e ON s.student_id = e.student_id
JOIN section se ON e.section_id = se.section_id
JOIN course c ON se.course_id = c.course_id
JOIN term t ON se.term_id = t.term_id
JOIN faculty fa ON se.faculty_id = fa.faculty_id
WHERE t.name = 'Fall' AND t.year = 2019
GROUP BY fname, lname
HAVING Credits > 3
ORDER BY credits desc
 ;