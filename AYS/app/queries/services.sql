CREATE DATABASE `AYS`;

USE `AYS`;

CREATE TABLE `ServiceCategory`
(
    `service_category_id` INT NOT NULL AUTO_INCREMENT,
    `service_category_name` VARCHAR(100) NOT NULL,

    PRIMARY KEY (`service_category_id`)
);

CREATE TABLE `ServiceType`
(
    `service_type_id` INT NOT NULL AUTO_INCREMENT,
    `service_type_name` VARCHAR(100) NOT NULL,
    `service_category` INT NOT NULL,

    PRIMARY KEY (`service_type_id`),
    FOREIGN KEY (`service_category`) REFERENCES `ServiceCategory` (`service_category_id`)
);

CREATE TABLE `Service`
(
    `service_id` INT NOT NULL AUTO_INCREMENT,
    `service_title` VARCHAR(100) NOT NULL,
    `service_description` TEXT NOT NULL,
    `service_user_id` INT NOT NULL,
    `service_user_rating` INT NOT NULL,
    `service_user_level` INT NOT NULL,
    `service_user_is_trusted` BOOLEAN,
    `service_date_posted` DATE NOT NULL,
    `service_schedule` DATE NOT NULL,
    `service_location` VARCHAR(100) NOT NULL,
    `service_type` INT NOT NULL,
    `service_amount` FLOAT(20, 2) NOT NULL,

    PRIMARY KEY (`service_id`),
    FOREIGN KEY (`service_type`) REFERENCES `ServiceType` (`service_type_id`)
);

INSERT INTO `ServiceCategory` (`service_category_name`)
VALUES ('Education');

INSERT INTO `ServiceType` (`service_type_name`, `service_category`)
VALUES ('Class', 1);

INSERT INTO `Service` (`service_title`, `service_description`, `service_user_id`, `service_user_rating`, `service_user_level`, `service_user_is_trusted`, `service_date_posted`, `service_schedule`, `service_location`, `service_type`, `service_amount`)
VALUES ('Aoi no Zen Garden', 'This is a free Japanese class tutorial for beginners!', 0, 5, 1, true, '2000-12-20', '2000-12-25', 'Tokyo Japan', 1, 0.00);
