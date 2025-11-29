from textual.app import App, ComposeResult
from textual.containers import Vertical, VerticalScroll, Horizontal
from textual.reactive import reactive
from textual.widgets import Static, Button
from dotenv import load_dotenv

from .components.header import CustomHeader
from .screens.entry import Entry

import os


load_dotenv()


VERSION = os.getenv("VERSION", "0.1.0")


class TodoTui(App):
    todo_items = reactive([])
    selected_todo_id = reactive('')

    def __init__(self, todo_service) -> None:
        super().__init__()

        self.todo_service = todo_service

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id

        match button_id:
            case "new":
                self.push_screen(Entry(self.todo_service))
            
            case "edit":
                self.notify("Edit Todo Entry not implemented yet", timeout=5)
            
            case "delete":
                self.notify("Delete Todo Entry not implemented yet", timeout=5)
            
            case "exit":
                self.exit()

    def on_mount(self) -> None:
        self.query_one("#todo-list", VerticalScroll).loading = True

        self.title = "ToDo - TUI"
        self.todo_items = self.todo_service.get_todo_items()

        if not self.todo_items or len(self.todo_items) == 0:
            self.query_one("#todo-list", VerticalScroll).mount(
                Vertical(
                    Static("No Todo Items Created Yet..."),
                ),
                Vertical(
                    Static("Create A New Todo Item with the 'New' Button"),
                ),
            )

            self.query_one("#todo-list", VerticalScroll).loading = False

        else:
            # display todo items
            self.query_one("#todo-list", VerticalScroll).loading = False

    def compose(self) -> ComposeResult:
        yield CustomHeader(
            show_clock = True,
            icon = f'v{VERSION}',
            name = "ToDo - TUI",
            screen_title = "ToDo - TUI",
            tall = True,
        )

        yield Vertical(
            Vertical(
                VerticalScroll(id="todo-list"),
            ),
            Horizontal(
                Button("New", id="new"),
                Button("Edit", id="edit"),
                Button("Exit", id="exit"),
            ),
        )
