from talon import Module, Context, actions

mod = Module()
active = False
ctx = Context()
ctx.matches = """
os: windows
and app.name: /HireTrack/
"""

@mod.capture(rule="tech | operator lighting | operator audio | operator visual | operate camera | operator audio visual")
def crew_type(m) -> str:
    """
    Matches the transport vehicle as a van or truck.
    """
    m = str(m)
    if m.lower() == "tech":
        m = "Tech Audio-Visual"
    elif m.lower() == "operator lighting":
        m = "Operator Lighting"
    elif m.lower() == "operator audio":
        m = "Operator Audio"
    elif m.lower() == "operator visual":
        m = "Operator Visual"
    elif m.lower() == "operator camera":
        m = "Operator Camera"
    elif m.lower() == "operator audio visual":
        m = "Operator Aud-Visual"
    return m

@mod.capture(rule="<number>")
def crew_quantity(m) -> int:
    """
    Captures a number and returns it as an integer.
    """
    return int(m.number)


@mod.action_class
class Actions:

    def edit_crew_type(crew_type: str = "Tech Audio-Visual"):
        """Edits the crew type on the current crew area in the crew editor."""
        actions.user.grid_win("871")
        actions.mouse_click()
        actions.insert(crew_type)
        actions.key("enter")

    def edit_crew_quantity(quantity: int = 1):
        """Edits the crew quantity in the current crew area in the crew editor."""
        actions.user.grid_win("781")
        actions.mouse_click()
        actions.edit.select_all()
        actions.edit.delete()
        actions.insert(quantity)
        actions.key("enter")

    def edit_crew_start():
        """Edits the start time for the crew area in the crew editor."""
        actions.user.grid_win("7299")
        actions.mouse_click()

    def edit_crew_end():
        """Edits the end time for the crew area in the crew editor."""
        actions.user.grid_win("8199")
        actions.mouse_click()

    def crew_apply():
        """Applies the edits from the crew editor to the crew area."""
        actions.user.grid_win("322")
        actions.mouse_click()
        actions.user.disable_tag("user.htcreweditor")
        actions.user.enable_tag("user.htquote")
        