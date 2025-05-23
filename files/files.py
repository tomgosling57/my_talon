from talon import actions, Module
from time import sleep

mod = Module()

@mod.action_class
class Actions:
    def open_file_in_code(path: str):
        """Opens the given file in VS Code using Command Prompt."""
        actions.key("win-r")
        sleep(.1)
        actions.insert(f"code \"{path}\"")
        actions.key("enter")