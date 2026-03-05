-- Creates the MySQL server user user_0d_1 with all privileges
-- The password is set to user_0d_1_pwd
-- If the user already exists, the script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';