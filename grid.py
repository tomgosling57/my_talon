from talon import Module, Context, actions

mod = Module()
active = False
ctx = Context()
ctx.matches = """
os: windows
"""

@mod.action_class
class Actions:
    def grid_win(grid_numbers: str):
        """Activates the mouse grid over the currently active window and moves to the given grid numbers."""    
        actions.user.grid_activate()
        actions.user.grid_place_window()
        actions.user.grid_narrow_list(grid_numbers)
        actions.user.grid_close()