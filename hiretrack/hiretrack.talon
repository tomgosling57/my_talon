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

toggle crm: user.toggle_tag("user.htcrm")
    

