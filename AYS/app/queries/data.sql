INSERT INTO `User` (`user_id`, `user_password`, `user_account_type`, `user_rating`, `user_level`, `user_is_trusted`, `user_first_name`, `user_middle_name`, `user_last_name`)
VALUES ('aoi_suzuki', '1234', 'SP', 3.45, 1, true, 'Aoi', '', 'Suzuki');

INSERT INTO `User` (`user_id`, `user_password`, `user_account_type`, `user_rating`, `user_level`, `user_is_trusted`, `user_first_name`, `user_middle_name`, `user_last_name`)
VALUES ('aoi_suzuki1', '1234', 'SP', 4.5, 1, true, 'Aoi', '', 'Suzuki');

INSERT INTO `User` (`user_id`, `user_password`, `user_account_type`, `user_rating`, `user_level`, `user_is_trusted`, `user_first_name`, `user_middle_name`, `user_last_name`)
VALUES ('aoi_suzuki2', '1234', 'SP', 5.00, 1, true, 'Aoi', '', 'Suzuki');

INSERT INTO `ServiceCategory` (`service_category_name`)
VALUES ('Education');

INSERT INTO `ServiceType` (`service_type_name`, `service_category`)
VALUES ('Class', 1);

INSERT INTO `ServicePost` (`service_post_title`, `service_post_description`, `service_post_user`, `service_post_date_posted`, `service_post_schedule`, `service_post_location`, `service_post_type`, `service_post_amount`)
VALUES ('Aoi no Zen Garden', 'This is a free Japanese class tutorial for beginners!', 'aoi_suzuki', '2000-12-20', '2000-12-25', 'Tokyo Japan', 1, 1.99);

INSERT INTO `ServicePost` (`service_post_title`, `service_post_description`, `service_post_user`, `service_post_date_posted`, `service_post_schedule`, `service_post_location`, `service_post_type`, `service_post_amount`)
VALUES ('Aoi no Zen Garden', 'This is a free Japanese class tutorial for beginners!', 'aoi_suzuki1', '2000-12-20', '2000-12-25', 'Tokyo Japan', 1, 1.99);

INSERT INTO `ServicePost` (`service_post_title`, `service_post_description`, `service_post_user`, `service_post_date_posted`, `service_post_schedule`, `service_post_location`, `service_post_type`, `service_post_amount`)
VALUES ('Aoi no Zen Garden', 'This is a free Japanese class tutorial for beginners!', 'aoi_suzuki2', '2000-12-20', '2000-12-25', 'Tokyo Japan', 1, 1.99);