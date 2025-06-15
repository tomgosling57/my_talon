from time import sleep
from talon import Module, actions

mod = Module()

# Define App Context
mod.apps.illustrator = """
os: windows
and app.name: /Adobe Illustrator 2023/
and app.exe: Adobe Illustrator 2023.exe
"""

@mod.action_class
class Actions:
    def illustrator_set_sidebar_width():
        """Sets the width of the sidebar in illustrator"""
        actions.user.grid("656")
        actions.mouse_click()
        actions.mouse_release()
            