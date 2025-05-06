CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

-- Users Table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Books Table
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    category VARCHAR(100),
    total_copies INT NOT NULL,
    available_copies INT NOT NULL
);

-- Loans Table
CREATE TABLE Loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    loan_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Sample Data
INSERT INTO Users (name, email) VALUES ('Alice', 'alice@example.com'), ('Bob', 'bob@example.com');
INSERT INTO Books (title, author, category, total_copies, available_copies)
VALUES ('1984', 'George Orwell', 'Fiction', 5, 5),
       ('Clean Code', 'Robert C. Martin', 'Programming', 3, 3);
