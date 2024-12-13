from talon import Module

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
mod.tag("htcrewmenu", desc="Commands to execute within the crew menu in Hiretrack")

mod.list("ht_job_types", "The list of job types a Hiretrack quote can have.")