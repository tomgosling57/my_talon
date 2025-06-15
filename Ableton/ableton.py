from time import sleep
from talon import Module, actions

mod = Module()

# Define App Context
mod.apps.Ableton = """
os: windows
and app.name: /Ableton Live 11 Standard/
and app.exe: Ableton Live 11 Standard.exe
"""

# Declare tags for hiretrack
mod.tag("Ableton", desc="Commands to execute in Ableton.")
