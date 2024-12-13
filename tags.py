from talon import Module, Context

mod = Module()
active = False
ctx = Context()
ctx.matches = """
os: windows
"""

@mod.action_class
class Actions:
    def enable_tag(tag: str):
        """Enables the given tag."""
        tags = list(ctx.tags)
        if tag not in ctx.tags:
            tags.append(tag)
        ctx.tags = frozenset(tags)

    def disable_tag(tag: str):
        """Disables the given tag."""
        tags = list(ctx.tags)
        if tag in ctx.tags:
            tags.remove(tag)
        ctx.tags = frozenset(tags)

    def toggle_tag(tag: str):
        """Toggles the given tag."""
        
        tags = list(ctx.tags)
        
        if tag in ctx.tags:
            tags.remove(tag)

        else:
            tags.append(tag) 
        
        ctx.tags = frozenset(tags)
