from talon import Module, actions

mod = Module()

# Define App Context
mod.apps.outlook = """
os: windows
and app.name: /Outlook/
"""

@mod.action_class
class OutlookActions:
    def add_signature():
        """Signs the email with the third signature."""
        actions.user.grid_win("8734")
        actions.mouse_click()
        actions.user.multi_press_key("down", 3)
        actions.key("enter")

    def discard_email():
        """Discards the current draft email"""
        actions.user.grid_win("961")
        actions.mouse_click()

    def reply_email():
        """Replies to the current email."""
        actions.user.grid_win("928")
        actions.mouse_click()

    def edit_recipient():
        """Edits the recipient on the current email draft."""
    
    def select_outlook_results():
        """Selects the search results to an outlook."""
        actions.user.grid_win("73")
        actions.mouse_click()
 
    def outlook_home():
        """Selects the home toolbar in outlook."""
        actions.user.grid_win("7753")
        actions.mouse_click()
    
    def categorize_results():
        """Categorizes the selected results with quote done by tom."""
        actions.user.outlook_home()
        actions.user.grid_win("8911")
        actions.mouse_click()
        actions.user.multi_press_key("down", 9)        
        actions.key("enter")

    def categorize_all():
        """Categorizes all results with with quote done by tom."""
        actions.user.select_outlook_results()
        actions.key("ctrl-a")
        actions.user.categorize_results()
        actions.sleep(.5)
        actions.key("enter")

    def search_clipboard_outlook():
        """Searches the clipboard contents in outlook."""
        actions.user.grid_activate()
        actions.user.grid_place_window()
        actions.user.grid_narrow_list("7982")
        actions.mouse_click()
        actions.user.grid_close()
        actions.sleep(0.2)
        actions.key("ctrl-a delete")
        actions.key("ctrl-v enter")
