from time import sleep
from talon import Module, actions

mod = Module()

# Define App Context
mod.apps.vscode = """
os: windows
and app.name: /vscode/
"""
mod.tag("roo", desc="Commands to execute in roo code.")
mod.tag("roo_settings", desc="Commands to execute in the roo code settings tab.")

@mod.action_class
class Actions:
    
    def set_sidebar_width():
        """Sets the width of the sidebar granted the user has begun dragging the panel before calling the command."""
        actions.user.grid_win("46")
        actions.mouse_click()
        actions.mouse_release()
    
    def roo_select_profile():
        """Selects the profile used by roo code."""
        actions.user.grid_win("116")
        actions.mouse_click()   
        
    def roo_edit_profile(path: str):
        """Opens the specified profile editor in roo code."""
        actions.user.roo_select_profile()
        sleep(.5)
        actions.key("up")
        actions.key("enter")
        actions.insert(path)
        actions.key("enter")
        actions.user.enable_tag("roo_settings")
    
    def roo_settings():
        """Opens the setting tab in recode."""
        actions.user.grid_win("7946")
        actions.mouse_click()
        actions.user.enable_tag("user.roo_settings")
    
    def select_terminal_output():
        """Selects the output of the terminal."""
        actions.user.grid_win("2228")
        actions.mouse_drag()
        actions.user.grid_win("2888")
        