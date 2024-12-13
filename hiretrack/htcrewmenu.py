from talon import Module, actions

mod = Module()

# Define App Context
mod.apps.hiretrack = """
os: windows
and app.name: /HireTrack/
"""

@mod.action_class
class Actions:
    def open_crew():
        """Opens the crew tab."""
        actions.user.grid_win("758")
        actions.mouse_click()

    def add_crew_area():
        """Adds a new area in the crew tab."""
        actions.user.grid_win("751")
        actions.mouse_click()