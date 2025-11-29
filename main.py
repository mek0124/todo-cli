from tui.tui import TodoTui
from core.services.todo_service import TodoService
from core.storage.repository import TodoRepository


if __name__ == '__main__':
    todo_repository = TodoRepository()
    todo_service = TodoService(todo_repository)

    app = TodoTui(todo_service)
    app.run()