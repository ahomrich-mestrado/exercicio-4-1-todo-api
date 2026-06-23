# Exercício 4.1 — Todo API

API REST para gerenciamento de tarefas (todos) construída com FastAPI.

## Endpoints

| Método | Rota            | Descrição               |
|--------|-----------------|-------------------------|
| GET    | `/todos`        | Lista todas as tarefas  |
| POST   | `/todos`        | Cria uma nova tarefa    |
| GET    | `/todos/{id}`   | Busca uma tarefa por ID |
| PUT    | `/todos/{id}`   | Atualiza uma tarefa     |
| DELETE | `/todos/{id}`   | Remove uma tarefa       |

## Como executar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse a documentação interativa em: http://localhost:8000/docs
