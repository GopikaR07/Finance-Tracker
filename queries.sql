-- DATABASE CREATION

create database finance_tracker;

--USING THE DATABASE
use finance_tracker;

-- -------WORKING IN THE DATABASE--------------

--CREATING TABLES

create table users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);
create table expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category VARCHAR(50),
    amount DECIMAL(10, 2),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table goals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    goal_name VARCHAR(255),
    goal_amount DECIMAL(10, 2),
    amount_saved FLOAT,
    remaining_budget FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
