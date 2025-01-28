from time import sleep
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
    
    def open_quote():
        """Opens the quote for the equipment list."""
        actions.user.grid_win("77399")
        actions.mouse_click()
        actions.user.disable_tag("user.hteqlist")
        actions.user.enable_tag("user.htquote")
    
    def edit_date_out():
        """Edits the outdate for the equipment list."""
        actions.user.grid_win("7662")
        actions.mouse_click()

    def edit_date_back():
        """Edits the back date for the equipment list."""
        actions.user.grid_win("7362")
        actions.mouse_click()

    def edit_setup():
        """Edits the setup time for the equipment list."""
        actions.user.grid_win("763")
        actions.mouse_click()

    def edit_start():
        """Edits the start time for the equipment list."""
        actions.user.grid_win("7399")
        actions.mouse_click()

    def edit_end():
        """Edits the end time for the equipment list."""
        actions.user.grid_win("739")
        actions.mouse_click()

    def edit_removal():
        """Edits the derig time for the equipment list."""
        actions.user.grid_win("7368")
        actions.mouse_click()

    def fix_eq_date_out():
        """Sets the time to midday on the outdate for the equipment list"""
        actions.user.edit_date_out()
        actions.insert("1200")
        actions.key("enter")
    
    def fix_eq_date_back():
        """Sets the time to midday on the back date for the equipment list."""
        actions.user.edit_date_back()
        actions.insert("1200")
        actions.key("enter")

    def edit_venue():
        """Edits the venue of the equipment list."""
        actions.user.grid_win("728")
        actions.mouse_click()
    
    def venue_customer_pickup()    :
        """Sets the venue of the equipment list to customer pickup at Wwave."""
        actions.user.edit_venue()
        actions.insert("customer pick up from")

    def open_public_notes():
        """Opens the public notes of the equipment list."""
        actions.user.grid_win("7293")
        actions.mouse_click()
        actions.user.enable_tag("user.hteqlistnotes")

    def open_private_notes():
        """Opens the private notes of the equipment list."""
        actions.user.grid_win("72733")
        actions.mouse_click()
        actions.user.enable_tag("user.hteqlistnotes")

    def close_notes():
        """Closes the notes in the equipment list"""
        actions.user.grid_win("334")
        actions.mouse_click()
        actions.user.disable_tag("user.hteqlistnotes")

    def add_equipment():
        """Opens the equipment menu to add equipment to the list."""
        actions.user.grid_win("5588")
        actions.mouse_click()
    
    def cancel_equipment():
        """Closes the equipment menu and does not apply any changes."""
        actions.user.grid_win("326")
        actions.mouse_click()

    def apply_equipment():
        """Closes the equipment menu and applies changes."""
        actions.user.grid_win("33")
        actions.mouse_click()
    
    def toggle_auto_reopen_equipment():
        """Toggles the order reopen feature for the equipment menu."""
        actions.user.grid_win("33964")
        actions.mouse_click()

    def add_damage_waver():
        """Adds a damage waiver to the equipment list."""
        actions.user.grid_win("81564")
        actions.mouse_click()
        sleep(.2)
        actions.user.grid_win("256")
        actions.mouse_click()
        actions.key("down")
        actions.key("down")
        actions.key("down")
        actions.key("enter")
        actions.user.grid_win("336")
        actions.mouse_click()

    def we_deliver():
        """Toggles the 'we deliver' option on the equipment list."""
        actions.user.grid_win("82224")
        actions.mouse_click()

    def we_collect():
        """Toggles the 'we collect' option on the equipment list."""
        actions.user.grid_win("8233")
        actions.mouse_click()
    
    def equipment_add():
        """Adds this selected equipment in the equipment selected to the equipment list."""
        actions.user.grid_win("33")
        actions.mouse_click()