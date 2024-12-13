from time import sleep
from talon import Module, Context, actions

mod = Module()
active = False
ctx = Context()
ctx.matches = """
os: windows
and app.name: /HireTrack/
"""


@mod.capture(rule="Delivery | Pickup")
def transport_type(m) -> str:
    """
    Matches the transport types delivery or pickup.
    """
    m = str(m)
    m = m[0].upper() + m[1:]
    return str(m)

@mod.capture(rule="van | truck | car")
def transport_vehicle(m) -> str:
    """
    Matches the transport vehicle as a van or truck.
    """
    m = str(m)
    if m.lower() == "van":
        m = "large van"
    elif m.lower() == "truck":
        m = "3 tonne truck"
    return m

@mod.capture(rule="lower | upper")
def transport_line_type(m) -> str:
    """
    Matches the transport line type as upper or lower.
    """
    return str(m)

@mod.action_class
class Actions:
    def edit_job_date_out():
        """Edits the job date out field on a open quote"""
        actions.user.grid_win("576")
        actions.mouse_click()

    def edit_job_date_back():
        """Edits the date back field on a open quote."""
        actions.user.grid_win("5728")
        actions.mouse_click()

    def set_datetime_midday():
        """Changes the job date out time to 12 PM"""
        actions.edit.line_end()
        for i in range(4):
            actions.edit.delete()
        actions.insert("1200")

    def set_job_type(job_type: str):
        """Edits the job type of the open quote to the value of job_type"""
        actions.user.grid_win("81588")
        actions.mouse_click()
        actions.edit.select_all()
        actions.insert(job_type)

    def fix_job_date_out():
        """Set the time of job date out to midday."""
        actions.user.edit_job_date_out()
        actions.user.set_datetime_midday()
        
    def fix_job_date_back():
        """Set the time of job date back to midday."""
        actions.user.edit_job_date_back()
        actions.user.set_datetime_midday()
        
    def fix_job_dates():
        """Set the time of job date out and date back to midday."""
        actions.user.fix_job_date_back()
        actions.user.fix_job_date_out()

    def set_handler():
        """Set the handler of the job to tom gosling"""
        actions.user.grid_win("5777")
        actions.mouse_click()
        actions.edit.select_all()
        actions.insert("tom gosling")
        actions.key("enter")

    def set_status():
        """Edits the status of the open job."""
        actions.user.grid_win("8152")
        actions.mouse_click()

    def prep_job_contact():
        """Prepares the job contact by setting it as the main contact for the job and updating the mobile field with the telephone number."""
        
        # Opening contact window
        actions.user.grid_win("43717")
        actions.mouse_click()
        actions.sleep(.5)
        actions.key("down")

        # Selecting first available contact
        actions.user.grid_win("8858")
        actions.mouse_click()
        actions.mouse_click()
        
        # Copying telephone field
        actions.user.grid_win("528")
        actions.mouse_click()
        actions.edit.select_line()
        actions.key("ctrl-c")

        # Pasting the telephone value in the mobile field
        actions.user.grid_win("28")
        actions.mouse_click()
        actions.key("ctrl-v")

        # Setting contact as main job contact
        actions.user.grid_win("162")
        actions.mouse_click()

        # Saving contact data
        actions.user.grid_win("32")
        actions.mouse_click()

    def open_rental():
        """Opens the rental panel inside of a job."""
        actions.user.grid_win("757")
        actions.mouse_click()

    def open_equipment_list():
        """Opens the rental panel and the first equipment list."""
        actions.user.open_rental()
        actions.user.grid_win("8282")
        actions.mouse_click()
        actions.mouse_click()
        actions.user.enable_tag("user.hteqlist")
        actions.user.disable_tag("user.htquote")

    def create_equipment_list():
        """Opens the rental panel and creates an equipment list."""
        actions.user.grid_win("751")
        actions.mouse_click()
        actions.user.disable_tag("user.htquote")
        actions.user.enable_tag("user.hteqlist")
    
    def open_transport():
        """Opens the transport panel."""
        actions.user.grid_win("759")
        actions.mouse_click()
    
    def open_general():
        """Opens the general panel."""
        actions.user.grid_win("7493")
        actions.mouse_click()

    def multi_press_key(key:str, n_times:int):
        """press the provided key the amount of times specified by n_times."""
        for i in range(n_times):
            actions.key(key)

    def transport_line(transport_type: str, vehicle: str = "large van", price: float = 80., line_type: str = "upper"):
        """Adds a new transport line and fills in the details on the lower line."""

        line_start_coordinates = {
            "upper": "727",
            "lower": "484"
        }
        include_coordinates = {
            "upper": "93934",
            "lower": "69661"
        }

        print(f"Line Type: {line_type}")
        # Creating a new line and setting the titles to line_type
        actions.user.grid_win("8552")
        actions.mouse_click()
        actions.insert(transport_type)
        actions.key("tab")
        actions.insert(transport_type)

        # Selecting the line and entering the line details
        actions.user.grid_win(line_start_coordinates[line_type])
        actions.mouse_click()
        sleep(.5)
        actions.key("enter")
        actions.insert("1") # Line Quantity
        actions.user.multi_press_key("tab", 2)
        actions.insert(vehicle) # Vehicle Type
        actions.key("tab")
        trip_mode = transport_type

        if transport_type.lower() in ["pickup", "pick up"]:
            trip_mode = "collect only"
        actions.insert(trip_mode) # Trip Mode
        actions.user.multi_press_key("tab", 2)
        actions.user.multi_press_key("enter", 2)
        actions.key("end")
        [actions.edit.delete() for x in range(4)]       
        actions.insert("14") # Trip returned datetime
        [actions.key("tab") for x in range(4)]
        actions.insert(price)
        actions.user.grid_win(include_coordinates[line_type]) # Click include on quote
        actions.mouse_click()

    def transport_delete_record():
        """Deletes the first transport record."""
        actions.user.grid_win("18166")
        actions.mouse_click()
        sleep(.2)
        actions.key("enter")