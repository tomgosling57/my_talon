app: hiretrack
tag: user.htcrm
-
prep crm:
    mimic("grid win")
    sleep(.2)
    mimic("seven six two touch")
    sleep(.2)
    mimic("word tom space word gosling")
    sleep(.2)
    mimic("grid win")
    sleep(.2)
    mimic("four five eight touch")
    sleep(.2)
    mimic("select line control cap")
    sleep(.2)
    mimic("grid win")
    sleep(.2)
    mimic("eight four four touch")
    sleep(.2)
    mimic("enter")
    user.disable_tag("user.htcrm")
    user.disable_tag("user.htlocate")
    user.enable_tag("user.htquote")

[copy] email:
    user.grid_activate()
    user.grid_place_window()
    user.grid_narrow_list("458")
    mouse_click()
    user.grid_close()
    edit.line_start()
    edit.extend_line_end()
    key("ctrl-c")
    sleep(.2)
    

open job:
    mimic("grid win")
    sleep(.2)
    mimic("nine six six touch")
    user.disable_tag("user.htcrm")
    user.disable_tag("user.htlocate")
    user.enable_tag("user.htquote")

search email:
    mimic("copy email")
    mimic("focus outlook")
    mimic("search clip")