app: outlook
-
search:
    user.grid_activate()
    user.grid_place_window()
    user.grid_narrow_list("7982")
    mouse_click()
    user.grid_close()
    sleep(0.2)
    key("ctrl-a delete")

clip:
    key("ctrl-v enter")