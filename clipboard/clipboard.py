from talon import Module, actions, Context
from time import sleep

ctx = Context()
ctx.matches = """
os: windows
mode: command
"""

mod = Module()

@mod.action_class
class Actions:
    
    def create_new_note():
        """Copies the selected text into a draft window."""
        actions.key("ctrl-c")
        actions.user.grid("111")
        actions.mouse_click()
        sleep(.5)
        actions.insert("notepad")
        sleep(.5)
        actions.key("enter")
        