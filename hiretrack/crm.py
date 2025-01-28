from talon import Module, Context, actions

mod = Module()
active = False
ctx = Context()
ctx.matches = """
os: windows
and app.name: /HireTrack/
"""

@mod.action_class
class Actions:
    def enable_crm_tag():
        """Enables the user.htcrm tag."""
        tags = list(ctx.tags)
        if "user.htcrm" not in ctx.tags:
            tags.append("user.htcrm")
        ctx.tags = frozenset(tags)

    def disable_crm_tag():
        """Disables the user.htcrm tag."""
        tags = list(ctx.tags)
        if "user.htcrm" in ctx.tags:
            tags.remove("user.htcrm")
        ctx.tags = frozenset(tags)

    def toggle_crm_tag():
        """Toggles the user.htcrm tag."""
        
        tags = list(ctx.tags)
        if "user.htcrm" in ctx.tags:
            tags.remove("user.htcrm")

        else:
            tags.append("user.htcrm") 
            
        ctx.tags = frozenset(tags)

    def copy_crm_email():
        """Copy the email of the open crm."""
        actions.user.grid_activate()
        actions.user.grid_place_window()
        actions.user.grid_narrow_list("458")
        actions.mouse_click()
        actions.user.grid_close()
        actions.edit.line_start()
        actions.edit.extend_line_end()
        actions.key("ctrl-c")

    def edit_crm_status():  
        """Edits the status of the currently open CRM."""          
        actions.user.grid_activate()
        actions.user.grid_place_window()
        actions.user.grid_narrow_list("7282")
        actions.mouse_click() 
        actions.user.grid_close()
        actions.edit.select_line()

    def refresh_view():
        """Refreshes the view of the crm list"""
        actions.user.grid_win("7669")
        actions.mouse_click()
        