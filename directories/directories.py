from talon import actions, Module
from time import sleep
mod = Module()

@mod.action_class
class Actions:
    def run_directory(path: str):
        """Opens the given directory using Run dialog."""
        actions.key("win-r")
        sleep(.1)
        actions.insert(path)
        actions.key("enter")