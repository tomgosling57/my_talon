app: hiretrack
tag: user.hteqlist
-
open quote:
    user.open_quote()

add damage waver:
    user.add_damage_waver()

add equipment:
    user.add_equipment()
equipment cancel:
    user.cancel_equipment()
equipment add:
    user.apply_equipment()
equipment toggle reopen:
    user.toggle_auto_reopen_equipment()

we deliver:
    user.we_deliver()
we collect:
    user.we_collect()

edit venue:
    user.edit_venue()
venue [customer] pickup:
    user.venue_customer_pickup()

open public notes:
    user.open_public_notes()

open private notes:
    user.open_private_notes()

edit [date] out: 
    user.edit_date_out()
edit [date] back:
    user.edit_date_back()
edit setup:
    user.edit_setup()
edit start:
    user.edit_start()
edit end:
    user.edit_end()
edit removal | derig:
    user.edit_removal()

fix [date] out:
    user.fix_eq_date_out()
fix [date] back:
    user.fix_eq_date_back()

tab close:
    user.grid_win("9938")
    mouse_click()
    user.disable_tag("user.htquote")
    user.disable_tag("user.hteqlist")

equipment add:
    user.equipment_add()