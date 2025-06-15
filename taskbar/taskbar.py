from time import sleep
from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def taskbar_network_settings():
        """Opens the network settings on the taskbar."""
        actions.user.grid("3324")
        sleep(.1)
        actions.mouse_click()
    