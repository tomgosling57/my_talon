from time import sleep
from talon import Module, actions

mod = Module()

# Define App Context
mod.apps.photoshop = """
os: windows
and app.name: /Adobe Photoshop 2025/
and app.exe: Adobe Photoshop 2025.exe
"""

@mod.action_class
class Actions:

    def hover_layers():
        """Hovers over the layers in the layer list."""
        actions.user.grid_leave_open("3")

    def photoshop_edit():
        """Opens the edit menu in photoshop."""
        actions.user.grid_win("778")
        actions.mouse_click()

    def photoshop_file():
        """Opens the file menu in photoshop."""
        actions.user.grid_win("7776")
        actions.mouse_click()
    
    def photoshop_image():
        """Opens the image menu in photoshop."""
        actions.user.grid("7786")
        actions.mouse_click()
    
    def photoshop_layer():
        """Opens the layer menu in photoshop."""
        actions.user.grid("7796")
        actions.mouse_click()

    def photoshop_select():
        """Opens the select menu in photoshop."""
        actions.user.grid("787")
        actions.mouse_click()

    def photoshop_type():
        """Opens the type menu in photoshop."""
        actions.user.grid("787")
        actions.mouse_click()

    def photoshop_filter():
        """Opens the filter menu in photoshop."""
        actions.user.grid("7879")
        actions.mouse_click()
        

    def photoshop_view():
        """Opens the view menu in photoshop."""
        actions.user.grid("789")
        actions.mouse_click()

    def photoshop_window():
        """Opens the window menu in photoshop."""
        actions.user.grid("798")
        actions.mouse_click()

    def photoshop_filter_layers():
        """Opens the filter layers menu in photoshop."""
        actions.user.grid("6258")
        actions.mouse_click()

    def photoshop_transform_width():
        """Edits the transform width in photoshop."""
        actions.user.grid("7868")
        actions.mouse_click()
        actions.edit.select_all()

    def photoshop_transform_height():
        """Edits the transform height in photoshop."""
        actions.user.grid("7948")
        actions.mouse_click()
        actions.edit.select_all()
    
    def photoshop_transform_x():
        """Edits the transform x in photoshop."""
        actions.user.grid("7769")
        actions.mouse_click()
        actions.edit.select_all()

    def photoshop_transform_y():
        """Edits the transform y in photoshop."""
        actions.user.grid("7857")
        actions.mouse_click()
        actions.edit.select_all()    

    def photoshop_transform_angle():
        """Edits the transform angle in photoshop."""
        actions.user.grid_n_click("7959")
        actions.edit.select_all()

    def photoshop_fill():
        """Edits the layer value of the current layer."""
        actions.user.grid_n_click("3926")
        actions.edit.select_all()

    def photoshop_brush_opacity():
        """Edits the brush opacity in photoshop."""
        actions.user.grid_win_click("7944")
        actions.edit.select_all()
    def photoshop_transform_layer_x():
        """Edits the layer's x dimension."""
        actions.user.grid_win_click("932")
    def photoshop_transform_layer_y():
        """Edits the layer's y dimension."""
        actions.user.grid_win_click("6987")
    def photoshop_transform_layer_width():
        """Edits the layer's width."""
        actions.user.grid_win_click("9236")
    def photoshop_transform_layer_height():
        """Edits the layer's height."""
        actions.user.grid_win_click("6899")
    def photoshop_center_x():
        """Centers the layer horizontally."""
        actions.user.grid_n_click("7948")
    def photoshop_center_y():
        """Centers the layer vertically."""
        actions.user.grid_n_click("7967")
    def brush_tool():
        """Activates the brush tool."""
        actions.key("b")
    def marque_tool():
        """Activates the marque tool"""
        actions.key("m")
    def move_tool():
        """Activates the move tool."""
        actions.key("v")

    def lasso_tool():
        """Activates the lasso tool."""
        actions.key("l")

    def bucket_tool():
        """Activates the bucket tool."""
        actions.key("g")

    def zoom_tool():
        """Activates the zoom tool."""
        actions.key("z")

    def erase_tool():
        """Activates the erase tool."""
        actions.key("e")

    def rectangle_tool():
        """Activates the rectangle tool."""
        actions.key("u")