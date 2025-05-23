from time import sleep
from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:

    def hover_layers():
        """Hovers over the layers in the layer list."""
        actions.user.grid_win_leave_open("3")

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
        actions.user.grid_win("7786")
        actions.mouse_click()
    
    def photoshop_layer():
        """Opens the layer menu in photoshop."""
        actions.user.grid_win("7796")
        actions.mouse_click()

    def photoshop_select():
        """Opens the select menu in photoshop."""
        actions.user.grid_win("788")
        actions.mouse_click()

    def photoshop_type():
        """Opens the type menu in photoshop."""
        actions.user.grid_win("787")
        actions.mouse_click()

    def photoshop_filter():
        """Opens the filter menu in photoshop."""
        actions.user.grid_win("7886")
        actions.mouse_click()
        

    def photoshop_view():
        """Opens the view menu in photoshop."""
        actions.user.grid_win("789")
        actions.mouse_click()

    def photoshop_window():
        """Opens the window menu in photoshop."""
        actions.user.grid_win("798")
        actions.mouse_click()

    def photoshop_filter_layers():
        """Opens the filter layers menu in photoshop."""
        actions.user.grid_win("6258")
        actions.mouse_click()

    def photoshop_transform_width():
        """Edits the transform width in photoshop."""
        actions.user.grid_win("7946")
        actions.mouse_click()
        actions.edit.select_all()

    def photoshop_transform_height():
        """Edits the transform height in photoshop."""
        actions.user.grid_win("796")
        actions.mouse_click()
        actions.edit.select_all()
    
    def photoshop_transform_x():
        """Edits the transform x in photoshop."""
        actions.user.grid_win("785")
        actions.mouse_click()
        actions.edit.select_all()

    def photoshop_transform_y():
        """Edits the transform y in photoshop."""
        actions.user.grid_win("786")
        actions.mouse_click()
        actions.edit.select_all()    

    def photoshop_transform_angle():
        """Edits the transform angle in photoshop."""
        actions.user.grid_n_click("874")
        actions.edit.select_all()

    def photoshop_fill():
        """Edits the layer value of the current layer.""" 
        actions.user.grid_n_click("6322")
        actions.edit.select_all()

    def photoshop_brush_opacity():
        """Edits the brush opacity in photoshop."""
        actions.user.grid_n_click("7944")
        actions.edit.select_all()