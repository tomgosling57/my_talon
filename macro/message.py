import ctypes
from talon import actions, Context, Module
ctx = Context()
ctx.matches = """
os: windows
"""
mod = Module()

def show_message(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)

@mod.action_class
class Actions:
    
    def show_message(title: str, message: str):
        show_message(title, message)
        