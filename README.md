# MySQL CRUD Project - Library Management & Task Manager API

This project demonstrates how to create a **relational database** using **MySQL** and implement a **CRUD API** using **FastAPI** connected to MySQL. It features two parts:

1. **Library Management System** (Database Schema)
2. **Task Manager API** (CRUD operations)

## Project Overview

### **1. Library Management System (MySQL Database Schema)**

This part of the project includes the creation of a MySQL database schema for managing library data, which includes:

- **Users** – Library members (with email and name).
- **Books** – Information about books available in the library (title, author, category).
- **Loans** – Information about books checked out by users (loan date, return date).

### **2. Task Manager CRUD API (FastAPI + MySQL)**

This part implements a **Task Manager API** where users can:

- Create a task
- Read all tasks
- Update a task
- Delete a task

The API connects to a MySQL database to manage tasks in the system.

## Prerequisites

To run this project, you'll need the following:

- **MySQL** installed and running on your machine.
- **Python 3.7+** installed.
- **FastAPI** and **MySQL connector** installed in your Python environment.

### Installation

1. **Clone the repository:**

2. **Install Python dependencies:**
Use `pip` to install the necessary packages for FastAPI:



3. **Set up the MySQL Database:**
- Create a MySQL database called `library_db` for the library schema.
- Use the provided `library_schema.sql` to create the necessary tables and insert sample data.

```sql
-- Run the following in your MySQL client:
source library_schema.sql;

CREATE DATABASE IF NOT EXISTS task_manager;
USE task_manager;

CREATE TABLE Tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    is_done BOOLEAN DEFAULT FALSE
);
 
 uvicorn task_manager_api:app --reload


