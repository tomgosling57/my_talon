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

sign:
    user.add_signature()

discard:
    user.discard_email()

reply:
    user.reply_email()

go results:
    user.select_outlook_results()

home:
    user.outlook_home()

categorize selected:
    user.categorize_results()

categorize all:
    user.categorize_all()