app: hiretrack
-
prep crm:
    user.grid_activate()
    user.grid_place_window()
    user.grid_narrow_list("762")
    mouse_click()
    user.grid_close()
    insert("tom gosling")

    user.copy_crm_email()

    user.grid_activate()
    user.grid_place_window()
    user.grid_narrow_list("844")
    mouse_click()
    user.grid_close()
    key("enter")

    user.disable_tag("user.htcrm")
    user.disable_tag("user.htlocate")
    user.enable_tag("user.htquote")

[copy] email:
    user.copy_crm_email()
    

open job | quote:
    user.grid_win("966")
    mouse_click()
    user.grid_close()

    user.disable_tag("user.htcrm")
    user.disable_tag("user.htlocate")
    user.enable_tag("user.htquote")

search email:
    user.copy_crm_email()
    user.switcher_focus("outlook")
    user.search_clipboard_outlook()

tab close:
    user.grid_activate()
    user.grid_place_window()
    user.grid_narrow_list("9938")
    mouse_click()
    user.grid_close()
    key("enter")
    user.disable_tag("user.htcrm")
    user.disable_tag("user.htlocate")

close dont save:
    user.grid_activate()
    user.grid_place_window()
    user.grid_narrow_list("9938")
    mouse_click()
    user.grid_close()
    key("tab")
    key("enter")
    user.disable_tag("user.htcrm")
    user.disable_tag("user.htlocate")


edit status:
    user.edit_crm_status()

status sent:
    user.edit_crm_status()
    insert("quote sent")
    key("enter")

status contacted:
    user.edit_crm_status()
    insert("contacted")
    key("enter")

status follow first:
    user.edit_crm_status()
    insert("chasing")
    key("enter")

status follow second:
    user.edit_crm_status()
    insert("second")
    key("enter")

status lost: 
    user.edit_crm_status()
    insert("complete - lost")
    key("enter")
    
refresh view:
    user.refresh_view()