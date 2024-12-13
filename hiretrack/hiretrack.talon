app: hiretrack

-
open crm list:
    mimic("grid win")
    sleep(0.2)
    mimic("seven seven five eight touch")
    sleep(0.2)
    mimic("grid win")
    sleep(0.2)
    mimic("six touch")
    user.enable_tag("user.htcrm")
    
refresh view:
    mimic("grid win")
    sleep(0.2)
    mimic("seven six six nine touch")


tab close:
    user.grid_win("9938")
    mouse_click()
    key("enter")

search view:
    user.grid_win("7552")
    mouse_click()

change view:
    user.grid_win("7668")
    mouse_click()
    
job mode:
    user.enable_tag("user.htquote")

equipment mode:
    user.enable_tag("user.hteqlist")