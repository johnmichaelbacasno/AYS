CREATE DATABASE `AYS`;

USE `AYS`;

CREATE TABLE `User`
(
    `user_id` INT NOT NULL AUTO_INCREMENT,
    `user_name` VARCHAR(100) NOT NULL,
    `user_account_type` VARCHAR(2) NOT NULL,
    `user_rating` INT NOT NULL,
    `user_level` INT NOT NULL,
    `user_is_trusted` BOOLEAN,
    
    PRIMARY KEY (`user_id`)
);

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
    `service_user` INT NOT NULL,
    `service_date_posted` DATE NOT NULL,
    `service_schedule` DATE NOT NULL,
    `service_location` VARCHAR(100) NOT NULL,
    `service_type` INT NOT NULL,
    `service_amount` FLOAT(20, 2) NOT NULL,

    PRIMARY KEY (`service_id`),
    FOREIGN KEY (`service_user`) REFERENCES `User` (`user_id`),
    FOREIGN KEY (`service_type`) REFERENCES `ServiceType` (`service_type_id`)
);

INSERT INTO `User` (`user_name`, `user_account_type`, `user_rating`, `user_level`, `user_is_trusted`)
VALUES ('Aoi Suzuki', 'SP', 5, 1, true);

INSERT INTO `ServiceCategory` (`service_category_name`)
VALUES ('Education');

INSERT INTO `ServiceType` (`service_type_name`, `service_category`)
VALUES ('Class', 1);

INSERT INTO `Service` (`service_title`, `service_description`, `service_user`, `service_date_posted`, `service_schedule`, `service_location`, `service_type`, `service_amount`)
VALUES ('Aoi no Zen Garden', 'This is a free Japanese class tutorial for beginners!', 1, '2000-12-20', '2000-12-25', 'Tokyo Japan', 1, 0.00);
