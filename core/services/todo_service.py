from typing import List, Union, Tuple

from ..models.todo import TodoCreate, TodoResponse


class TodoService:
    def __init__(self, todo_repository) -> None:
        self.todo_repository = todo_repository

    def get_todo_items(self) -> Union[List[TodoResponse] | None, str]:
        try:
            all_todo_items = self.todo_repository.get_todo_items("todo.json")
            return [TodoResponse(**item) for item in all_todo_items]    

        except Exception as e:
            return None, f"[Error] Failed to save task item: {e}"
        
    def create_todo(self, new_todo: dict) -> Tuple[bool, TodoResponse | str]:
        try:
            all_todo_items = self.todo_repository.get_todo_items("todo.json")
            converted_items = [TodoResponse(**item) for item in all_todo_items]

            found_todo = [todo for todo in converted_items if todo.title == new_todo["title"]]

            if found_todo:
                return False, "Title Already Exists"

            save_todo = TodoCreate(
                title = new_todo["title"],
                details = new_todo["content"],
                priority = new_todo["priority"],
            )

            did_save, response = self.todo_repository.save_todo(save_todo)

            if not did_save:
                return False, response
            
            return True, TodoResponse(**save_todo.model_dump())
        
        except Exception as e:
            return False, f"[Error]: Failed to save todo item: {e}"