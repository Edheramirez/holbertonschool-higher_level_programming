-- creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server.
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that,
-- references to id of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS
cities(id INT AUTO_INCREMENT UNIQUE NOT NULL, state_id INT NOT NULL,
name VARCHAR(256), PRIMARY KEY (id),
FOREIGN KEY(state_id) REFERENCES states(id));
