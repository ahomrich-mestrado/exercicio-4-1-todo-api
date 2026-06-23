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


@app.get("/tarefas", response_model=List[TodoItemResponse])
def list_tarefas():
    return todos


@app.get("/tarefas/{tarefa_id}", response_model=TodoItemResponse)
def get_tarefa(tarefa_id: int):
    for todo in todos:
        if todo.id == tarefa_id:
            return todo
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.put("/tarefas/{tarefa_id}", response_model=TodoItemResponse)
def update_tarefa(tarefa_id: int, item: TodoItem):
    for i, todo in enumerate(todos):
        if todo.id == tarefa_id:
            todos[i] = TodoItemResponse(id=tarefa_id, **item.model_dump())
            return todos[i]
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
