from time import sleep
from talon import Module, actions

mod = Module()

# Define App Context
mod.apps.capcut = """
os: windows
and app.name: /CapCut/
and app.exe: CapCut.exe
"""

@mod.action_class
class Actions:
    def capcut_clip_video():
        """Clicks on the clip video menu."""
        actions.user.grid_win_click("984")
        
    def capcut_clip_audio():
        """Clicks on the clip audio menu."""
        actions.user.grid_win_click("98")
        
    def capcut_clip_speed():
        """Clicks on the clip speed menu."""
        actions.user.grid_win_click("986")
        
    def capcut_clip_animation():
        """Clicks on the clip animation menu."""
        actions.user.grid_win_click("994")
        
    def capcut_clip_adjust():
        """Clicks on the clip adjust menu."""
        actions.user.grid_win_click("99")
        