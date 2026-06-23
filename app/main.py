from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class TodoItem(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoItemResponse(TodoItem):
    id: int

todos: List[TodoItemResponse] = []
next_id = 1


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tarefas", response_model=TodoItemResponse, status_code=201)
def create_tarefa(item: TodoItem):
    global next_id
    new_todo = TodoItemResponse(id=next_id, **item.model_dump())
    todos.append(new_todo)
    next_id += 1
    return new_todo
