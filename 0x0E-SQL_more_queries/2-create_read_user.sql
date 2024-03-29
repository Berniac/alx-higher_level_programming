-- creates database hbtn_0d_2 and user user_0d_2
-- user should only have SELECT privilege in database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
