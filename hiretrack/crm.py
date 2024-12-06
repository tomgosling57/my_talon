from talon import Module, Context

mod = Module()
active = False
ctx = Context()
ctx.matches = """
os: windows
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
