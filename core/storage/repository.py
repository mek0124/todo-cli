from pathlib import Path
from typing import Tuple

import json
import os


class TodoRepository:

    def check_file_exists(self, file_name: str = None) -> str | None:
        curr_dir = Path(__file__).parent
        data_dir = curr_dir / "data"

        if not data_dir.exists():
            os.makedirs(data_dir, exist_ok=True)

        data_file = data_dir / file_name

        if not data_file.exists():
            with open(data_file, 'w+', encoding="utf-8-sig") as new_file:
                json.dump([], new_file, indent=2)

            return data_file
        
        return data_file


    def get_todo_items(self, file_name: str) -> Tuple[list | None, str]:
        file_path = self.check_file_exists(file_name)

        try:
            with open(file_path, 'r', encoding="utf-8-sig") as f:
                return json.load(f)
            
        except Exception as e:
            return None, f"[Error]: Failed to obtain todo items from storage {e}"