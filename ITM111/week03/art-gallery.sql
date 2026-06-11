-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema art-gallery
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `art-gallery` ;

-- -----------------------------------------------------
-- Schema art-gallery
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `art-gallery` DEFAULT CHARACTER SET utf8 ;
USE `art-gallery` ;

-- -----------------------------------------------------
-- Table `art-gallery`.`artist`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `art-gallery`.`artist` ;

CREATE TABLE IF NOT EXISTS `art-gallery`.`artist` (
  `artist_id` INT NOT NULL AUTO_INCREMENT,
  `fname` VARCHAR(45) NOT NULL,
  `mname` VARCHAR(45) NULL,
  `lname` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NULL,
  `dob` INT(4) NULL,
  `dod` INT(4) NULL,
  `local` ENUM('y', 'n') NULL,
  PRIMARY KEY (`artist_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `art-gallery`.`artwork`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `art-gallery`.`artwork` ;

CREATE TABLE IF NOT EXISTS `art-gallery`.`artwork` (
  `artwork_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `artyear` INT(4) NULL,
  `period` VARCHAR(25) NULL,
  `arttype` VARCHAR(25) NULL,
  `file` VARCHAR(45) NULL,
  `artist_id` INT NOT NULL,
  PRIMARY KEY (`artwork_id`),
  INDEX `fk_paint_artist1_idx` (`artist_id` ASC) VISIBLE,
  CONSTRAINT `fk_paint_artist1`
    FOREIGN KEY (`artist_id`)
    REFERENCES `art-gallery`.`artist` (`artist_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `art-gallery`.`keyword`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `art-gallery`.`keyword` ;

CREATE TABLE IF NOT EXISTS `art-gallery`.`keyword` (
  `keyword_id` INT NOT NULL AUTO_INCREMENT,
  `keyword` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`keyword_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `art-gallery`.`artwork_has_keyword`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `art-gallery`.`artwork_has_keyword` ;

CREATE TABLE IF NOT EXISTS `art-gallery`.`artwork_has_keyword` (
  `artwork_id` INT NOT NULL,
  `keyword_id` INT NOT NULL,
  PRIMARY KEY (`artwork_id`, `keyword_id`),
  INDEX `fk_artwork_has_keyword_keyword1_idx` (`keyword_id` ASC) VISIBLE,
  INDEX `fk_artwork_has_keyword_artwork1_idx` (`artwork_id` ASC) VISIBLE,
  CONSTRAINT `fk_artwork_has_keyword_artwork1`
    FOREIGN KEY (`artwork_id`)
    REFERENCES `art-gallery`.`artwork` (`artwork_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_artwork_has_keyword_keyword1`
    FOREIGN KEY (`keyword_id`)
    REFERENCES `art-gallery`.`keyword` (`keyword_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO artist VALUES
(NULL, 'Vincent',NULL, 'van Gogh', 'France', '1853', '1890', 'n'),
(NULL, 'Rembrandt','Harmenszoon', 'van Rijn', 'Netherlands', '1606', '1669', 'n') ,
(NULL, 'Leonardo','Lonzo', 'da Vinci', 'Italy', '1452', '1519', 'n') ,
(NULL, 'Venture',NULL, 'Coy', 'United States', '1965', NULL, 'y') ,
(NULL, 'Deborah',NULL, 'Gill', 'United States', '1970', NULL, 'y') ,
(NULL, 'Claude',NULL, 'Monet', 'France', '1840', '1926', 'n') ,
(NULL, 'Pablo',NULL, 'Picasso', 'Spain', '1904', '1973', 'n') ,
(NULL, 'Michelangelo','Simoni', 'van Gogh', 'Italy', '1475', '1564', 'n') ;

SELECT * FROM artist;

INSERT INTO artwork VALUES
	(NULL, 'Irises', 1889, 'Impressionism', 'Oil', 'irises.jpg', 1),
    (NULL, 'The Starry Night', 1889, 'Post-Impressionism', 'Oil', 'starrynight.jpg', 1),
    (NULL, 'Sunflowers', 1888, 'Post-impressionism', 'Oil', 'sunflowers.jpg', 1),
    
    (NULL, 'Night Watch', 1642, 'Baroque', 'Oil', 'nightwatch.jpg', 2),
    (NULL, 'Storm on the Sea of Galilee', 1633, 'Dutch Golden Age', 'Oil', 'stormgalilee.jpg', 2),
    
    (NULL, 'Head of a Woman', 1508, 'High Renaissance', 'Oil', 'headwoman.jpg', 3),
    (NULL, 'Last Supper', 1498, 'Renaissance', 'Tempra', 'lastsupper.jpg', 3),
    (NULL, 'Mona Lisa', 1517, 'Renaissance', 'Oil', 'monalisa.jpg', 3),
    
    (NULL, 'Hillside Stream', 2005, 'Modern', 'Oil', 'hillsidestream.jpg', 4),
    (NULL, 'Old Barn', 1992, 'Modern', 'Oil', 'oldbarn.jpg', 4),
    
    (NULL, 'Beach Baby', 1999, 'Modern', 'Watercolor', 'beachbaby.jpg', 5),
    
    (NULL, 'Women in the Garden', 1866, 'Impressionism', 'Oil', 'womengarden.jpg', 6),
    
    (NULL, 'Old Guitarist', 1904, 'Modern', 'Oil', 'guitarist.jpg', 7);
    
	SELECT * FROM artwork;
    
    INSERT INTO keyword VALUES
    (NULL, 'flowers'),
    (NULL, 'blue'),
    (NULL, 'landscape'),
    (NULL, 'girl'),
    (NULL, 'people'),
    (NULL, 'battle'),
    (NULL, 'boat'),
    (NULL, 'water'),
    (NULL, 'Christ'),
    (NULL, 'food'),
    (NULL, 'baby');
    
	SELECT * FROM keyword;
    
	INSERT INTO artwork_has_keyword VALUES
    (1,1),
    (2,2),
    (2,3),
    (3,1),
    (4,4),
    (4,5),
    (4,6),
    (5,7),
    (5,8),
    (5,5),
    (5,9),
    (6,4),
    (6,5),
    (7,10),
    (7,5),
    (7,9),
    (8,4),
    (8,5),
    (9,8),
    (9,3),
    (10,3),
    (11,8),
    (11,5),
    (11,11),
    (12,3),
    (12,5),
    (12,1),
    (13,2),
    (13,5);

    SELECT * FROM artwork_has_keyword;