from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, HorizontalGroup
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import (
    Static, 
    Input, 
    Button, 
    RadioButton, 
    TextArea
)
from datetime import datetime
 
 
class Entry(Screen):
    title = reactive('')
    content = reactive('')
    priority = reactive(0)

    def __init__(self, todo_service) -> None:
        super().__init__()

        self.todo_service = todo_service

    def handle_submit(self) -> None:
        new_todo = {
            "title": self.title,
            "content": self.content,
            "priority": self.priority
        }
        try:
            did_save, response = self.todo_service.create_todo(new_todo)

            if not did_save:
                return self.notify(
                    f"[Error]: Failed to save todo item: {response}",
                    title = "Failed To Save",
                    severity = "error",
                    timeout = 5
                )
            
            return self.notify(
                response,
                title = "Save Succeeded",
                severity = "success",
                timeout = 5
            )
        
        except Exception as e:
            return self.notify(
                f"[Error]: {e}",
                title = "Unknown Exception",
                severity = "error",
                timeout = 5
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id

        match button_id:
            case "back":
                self.dismiss()

            case "submit":
                self.handle_submit()

    def on_input_changed(self, event: Input.Changed) -> None:
        input_id = event.input.id
        input_value = event.input.value

        match input_id:
            case "title":
                self.title = input_value

            case "content":
                self.content = input_value

            case "radio-low":
                self.priority = 3

            case "radio-medium":
                self.priority = 2

            case "radio-high":
                self.priority = 1
 
    def compose(self) -> ComposeResult:
        yield Vertical(
            Vertical(
                Static("Title"),
                Input(
                    value = self.title,
                    placeholder = "Grocery List",
                    type = "text",
                    tooltip = "Max 50 Characters",
                    max_length = 50
                ),
                Static("Priority"),
                HorizontalGroup(
                    RadioButton("Low", value = 3, id="radio-low"),
                    RadioButton("Medium", value = 2, id="radio-medium"),
                    RadioButton("High", value = 1, id="radio-high"),
                ),
                Static("Details"),
                TextArea(
                    show_cursor = True,
                    show_line_numbers = True,
                    line_number_start = 1,
                    id = "content"
                )
            ),
            HorizontalGroup(
                Button("Back", id="back"),
                Button("Create", id="submit"),
            ),
        )