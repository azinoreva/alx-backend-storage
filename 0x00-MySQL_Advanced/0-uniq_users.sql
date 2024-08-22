-- SQL script that creates a table users
-- id, email and name 
CREATE TABLE IF NOT EXISTS Users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

