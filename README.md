# Flask TODO (TO: para, DO: fazer)

TODO list feito utilizando Flask com escrita em disco para estudos

## Qual a definição de pronto deste projeto?

- Expor um endpoint para acessar a lista de TODOs.
- GET /: retorna apenas um hello world
- POST /todos: Cria uma nova tarefa
- GET /todos: Retorna todas as tarefas
- GET /todos/:id: Retorna uma tarefa específica
- PUT /todos/:id: Atualiza uma tarefa
- DELETE /todos/:id: Deleta uma tarefa
- GET /todos/:id/done: Marca uma tarefa como concluída
- GET /todos/:id/undone: Marca uma tarefa como não concluída

## Rodando a aplicação

```bash
# Linux
export FLASK_APP=app
export FLASK_ENV=development
flask run

# Windows
set FLASK_APP=app
set FLASK_ENV=development
flask run
```

### Q&A

- O que é esse README.md?
R: md é uma extensão de Markdown que por sua vez é uma linguagem flexível e que permite escrever textos em várias linguagens.

- Como manipular arquivos com Python?
R: https://www.w3schools.com/python/ref_func_open.asp