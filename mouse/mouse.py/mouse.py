from talon import Module, actions, settings, Context

ctx = Context()
ctx.matches = """
os: windows
mode: command
"""

mod = Module()

@mod.action_class
class Actions:
    def hiss_scroll_stop():
        """Disables mouse hiss to scroll"""
        global hiss_scroll_active
        hiss_scroll_active = False



@ctx.action_class("user")
class UserActions:
    
    
    def hiss_scroll_up():
        """Change mouse hiss scroll direction to up"""
        global hiss_scroll_up
        global hiss_scroll_active
        hiss_scroll_active = True
        hiss_scroll_up = True


    def hiss_scroll_down():
        """Change mouse hiss scroll direction to down"""
        global hiss_scroll_up
        global hiss_scroll_active 
        hiss_scroll_active = True
        hiss_scroll_up = False

    # def noise_trigger_hiss(active: bool):
    #     global hiss_scroll_up
    #     global hiss_scroll_active
        
    #     if hiss_scroll_active == True:
    #         if settings.get("user.mouse_enable_hiss_scroll"):
    #             if active:
    #                 if hiss_scroll_up:
    #                     actions.user.mouse_scroll_up_continuous()
    #                 else:
    #                     actions.user.mouse_scroll_down_continuous()
    #             else:
    #                 actions.user.mouse_scroll_stop()

