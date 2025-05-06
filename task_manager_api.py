from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="task_manager"
)
cursor = conn.cursor(dictionary=True)

# Pydantic model
class Task(BaseModel):
    title: str
    description: str = ""
    is_done: bool = False

# Create Task
@app.post("/tasks/")
def create_task(task: Task):
    cursor.execute("INSERT INTO Tasks (title, description, is_done) VALUES (%s, %s, %s)",
                   (task.title, task.description, task.is_done))
    conn.commit()
    return {"message": "Task created successfully"}

# Read All Tasks
@app.get("/tasks/")
def get_tasks():
    cursor.execute("SELECT * FROM Tasks")
    return cursor.fetchall()

# Update Task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    cursor.execute("UPDATE Tasks SET title=%s, description=%s, is_done=%s WHERE task_id=%s",
                   (task.title, task.description, task.is_done, task_id))
    conn.commit()
    return {"message": "Task updated"}

# Delete Task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    cursor.execute("DELETE FROM Tasks WHERE task_id=%s", (task_id,))
    conn.commit()
    return {"message": "Task deleted"}
