from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

@app.get("/")
def root():
    return {"message": "ToDo API Running 🚀"}

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {"message": "Deleted"}