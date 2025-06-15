from talon import Module, actions
from time import sleep

mod = Module()

@mod.action_class
class Actions:
    
    def open_run():
        """Opens run."""
        actions.key("win-r")
    
    def run(path: str):
        """Opens the given directory using Run dialog.
        
        Args:
            path: The directory path to open
        """
        actions.user.open_run()
        sleep(.1)
        actions.insert(path)
        actions.key("enter")
    