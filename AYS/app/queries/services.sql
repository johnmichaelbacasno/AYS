CREATE DATABASE `AYS`;

USE `AYS`;

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
    `service_type` VARCHAR(50) NOT NULL,
    `service_category` VARCHAR(50) NOT NULL,
    `service_amount` INT NOT NULL,

    PRIMARY KEY (`service_id`)
);

INSERT INTO `Service` 
(
    `service_title`,
    `service_description`,
    `service_user_id`,
    `service_user_rating`,
    `service_user_level`,
    `service_user_is_trusted`,
    `service_date_posted`,
    `service_schedule`,
    `service_location`,
    `service_type`,
    `service_category`,
    `service_amount`
)
VALUES (
    'Mark Spa',
    'I love to read, hang out with friends, watch football, listen to music, and learn new things.',
    0,
    5,
    1,
    true,
    '2000-12-25',
    '2000-12-25',
    'Quezon City',
    'Beauty',
    'Spa and Salon',
    500
);