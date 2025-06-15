app: hiretrack

-
open crm list:
    user.open_crm_list()



search view:
    user.grid_win("7552")
    mouse_click()

change view:
    user.grid_win("7668")
    mouse_click()
    
job mode:
    user.toggle_tag("user.htquote")

equipment mode:
    user.toggle_tag("user.hteqlist")

crew mode:
    user.toggle_tag("user.htcreweditor")

hire track password: "tomgosling"