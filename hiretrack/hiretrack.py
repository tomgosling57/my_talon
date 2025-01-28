from time import sleep
from talon import Module, actions

mod = Module()

# Define App Context
mod.apps.hiretrack = """
os: windows
and app.name: /HireTrack/
"""

# Declare tags for hiretrack
mod.tag("htcrm", desc="Commands to execute on an open CRM in Hiretrack.")
mod.tag("htquote", desc="Commands to execute on an open quote in Hiretrack.")
mod.tag("hteqlist", desc="Commands to execute on an open equipment list in Hiretrack.")
mod.tag("htjobstatus", desc="Commands to execute while setting a job status in Hiretrack.")
mod.tag("hteqlistnotes", desc="Commands to Execute While Viewing Notes in a job in Hiretrack.")
mod.tag("htcreweditor", desc="Commands to execute within the creditor in Hiretrack")
mod.list("ht_job_types", "The list of job types a Hiretrack quote can have.")

@mod.action_class
class Actions:
    def open_crm_list():
        """Opens the CRM list from the toolbar."""
        actions.user.grid_win("7758")
        actions.mouse_click()
        sleep(.5)
        actions.user.grid_win("6")
        actions.mouse_click()
        actions.user.enable_tag("user.htcrm")
    