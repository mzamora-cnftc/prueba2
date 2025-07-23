from typing import Dict, Callable

class HotkeyManager:
    def __init__(self):
        self.hotkeys: Dict[str, Callable] = {}

    def register_hotkey(self, key_combination: str, action: Callable):
        self.hotkeys[key_combination] = action

    def execute_hotkey(self, key_combination: str):
        if key_combination in self.hotkeys:
            self.hotkeys[key_combination]()
        else:
            print(f"No action registered for hotkey: {key_combination}")

    def list_hotkeys(self):
        return self.hotkeys.keys()