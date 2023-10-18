-- Write a script that creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on your MySQL server.

-- create the hbtn_0d_usa DataBase
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- set the hbtn_0d_usa as the current using DataBase
USE hbtn_0d_usa;

-- create new tabel in the hbtn_0d_usa DataBase called states
CREATE TABLE IF NOT EXISTS states(
       id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
       `name` VARCHAR(256) NOT NULL);
