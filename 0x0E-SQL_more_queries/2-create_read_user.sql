-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

-- create a new database with the name hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create a new user with the name user_0d_2 at the localhost
CREATE USER IF NOT EXISTS
       'user_0d_2'@'localhost'
       IDENTIFIED BY "user_0d_2_pwd";

-- give the user user_0d_2 prevalge of SELECT on the hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
