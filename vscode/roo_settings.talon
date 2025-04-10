tag: user.roo_settings
-
rename profile:
    user.grid_win("7344")
    mouse_click()

cancel: 
    user.grid_win("4258")
    mouse_click()
    user.disable_tag("roo_settings")

discard [changes]: 
    user.grid_win("4292")
    mouse_click()
    user.disable_tag("roo_settings")

done: 
    user.grid_win("7912")
    mouse_click()
    

save: 
    user.grid_win("7833")
    mouse_click()
    