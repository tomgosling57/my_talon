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

    def grid_win_leave_open(grid_numbers: str):
        """Activates the mouse grid over the currently active window and moves to the given grid numbers. The grid will remain open."""
        actions.user.grid_activate()
        actions.user.grid_place_window()
        actions.user.grid_narrow_list(grid_numbers)
        
    
    def grid(grid_numbers: str):
        """Activates the mouse grid over the entire screen and moves to the given grid numbers."""    
        actions.user.grid_activate()
        actions.user.grid_narrow_list(grid_numbers)
        actions.user.grid_close()

    def grid_n_click(grid_numbers: str):
        """Activates the mouse grid and enters the given numbers and clicks."""
        actions.user.grid_close()
        actions.user.grid(grid_numbers)
        actions.mouse_click()
    def grid_win_click(grid_numbers: str):
        """Activates the mouse grid and enters the given numbers and clicks."""
        actions.user.grid_win(grid_numbers)
        actions.mouse_click()

    def grid_leave_open(grid_numbers: str):
        """Activates the mouse grid over the entire screen and moves to the given grid numbers, leaving grid open."""
        actions.user.grid_activate()
        actions.user.grid_narrow_list(grid_numbers)

    def grid_leave_open_click(grid_numbers: str):
        """Activates the mouse grid, moves to given numbers and clicks, leaving grid open."""
        actions.user.grid_leave_open(grid_numbers)
        actions.mouse_click()