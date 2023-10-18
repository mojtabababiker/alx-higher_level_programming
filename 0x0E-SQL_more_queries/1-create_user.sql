-- Write a script that creates the MySQL server user user_0d_1.

-- creating a new user and initailize it with authoniticate by string password.
CREATE USER IF NOT EXISTS
       'user_0d_1'@'localhost'
       IDENTIFIED BY 'user_0d_1_pwd';

-- set or grant son prevelages over the user_0d_1 as the root
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
