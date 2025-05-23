tag: user.roo_settings
app: vscode
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
    

save: 
    user.grid_win("759")
    mouse_click()

done: user.grid_n_click("767")