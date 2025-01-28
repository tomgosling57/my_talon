app: hiretrack
tag: user.htquote
-

prep job contact:
    user.prep_job_contact()

set job type [{user.ht_job_types}]:
    user.set_job_type(ht_job_types or "")

fix job date out:
    user.fix_job_date_out()

fix job date back:
    user.fix_job_date_back()

edit [job] date out:
    user.edit_job_date_out()
edit [job] date back:
    user.edit_job_date_back()

fix job dates:
    user.fix_job_dates()

set handler:
    user.set_handler()

set status:
    user.set_status()

update all with job status:
    user.grid_win("752")
    mouse_click()
    user.grid_win("32")
    mouse_click()

prep job [{user.ht_job_types}]:
    user.prep_job_contact()
    sleep(1)
    user.set_handler()
    user.fix_job_dates()
    user.set_job_type(ht_job_types or "")

open rental:
    user.open_rental()

open equipment [list]:
    user.open_equipment_list()

create equipment [list]:
    user.create_equipment_list()

print quote:
    user.grid_win("7733")
    mouse_click()
    sleep(.2)
    key("down")
    key("enter")
    key("enter")

print proforma:
    user.grid_win("7733")
    mouse_click()
    sleep(.2)
    key("down")
    key("enter")
    key("down")
    key("enter")    

draft email:
    user.grid_win("859")
    mouse_click()

set email template:
    user.win_resize_absolute(1000, 800)
    sleep(.2)
    user.grid_win("782")
    mouse_click()

send email:
    user.win_resize_absolute(1000, 800)
    sleep(.2)
    user.grid_win("7488")
    mouse_click()

    user.grid_win("91")
    mouse_click()
    key("down")
    key("enter")
    key("down")
    key("down")
    key("enter")   

    user.grid_win("968")
    mouse_click()

tab close:
    user.grid_win("9938")
    mouse_click()
    user.disable_tag("user.htquote")
    user.disable_tag("user.hteqlist")

open transport:
    user.open_transport()

open quote:
    user.open_quote()

open general:
    user.open_general()

open crew:
    user.open_crew()

crew add area:
    user.crew_add_area()

crew edit role:
    user.crew_edit_role()

prep crew <Installation | Removal>:
    user.prep_crew()

transport <user.transport_type> [<number>] [<user.transport_vehicle>] <user.transport_line_type>:
    user.transport_line(transport_type, transport_vehicle or "large van", number or 80, transport_line_type)


transport delete record:
    user.transport_delete_record()