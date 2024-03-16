-- Script that creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- set password for user_0d_1
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants all privileges on all databases of your MySQL server to user_0d_1.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';