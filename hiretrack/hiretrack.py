from talon import Module

mod = Module()

# Define App Context
mod.apps.hiretrack = """
os: windows
and app.name: /HireTrack/
"""

# Declare tags for hiretrack
mod.tag("htcrm", desc="Commands to execute on an open CRM in Hiretrack.")
mod.tag("htlocate", desc="Commands to execute in a locator in Hiretrack")
mod.tag("htquote", desc="Commands to execute on an open quote in Hiretrack.")
mod.tag("hteqlist", desc="Commands to execute on an open equipment list in Hiretrack.")