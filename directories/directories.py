from talon import Module, actions, settings
from time import sleep
mod = Module()

mod.setting("user", type=str, default="tomgo", desc="The current windows user")
@mod.action_class
class Actions:

    def open_textures():
        """Open textures directory"""
        actions.user.run(f"C:\\Users\\{settings.get('user.user')}\\Pictures\\Textures")

    def open_downloads():
        """Open downloads directory"""
        actions.user.run(f"C:\\Users\\{settings.get('user.user')}\\Downloads")

    def open_pictures():
        """Open pictures directory"""
        actions.user.run(f"C:\\Users\\{settings.get('user.user')}\\Pictures")

    def open_desktop():
        """Open desktop directory"""
        actions.user.run(f"C:\\Users\\{settings.get('user.user')}\\Desktop")

    def open_documents():
        """Open documents directory"""
        actions.user.run(f"C:\\Users\\{settings.get('user.user')}\\Documents")

    def open_baz_ravish():
        """Open Baz Ravish directory"""
        actions.user.run("F:\\Baz Ravish")

    def open_baz_web():
        """Open Baz web directory"""
        actions.user.run("F:\\Baz Ravish\\baz_web")

    def open_baz_ravish_art():
        """Open Baz Ravish art directory"""
        actions.user.run("F:\\Baz Ravish\\Art")

    def open_baz_ravish_photos():
        """Open Baz Ravish photos directory"""
        actions.user.run("F:\\Baz Ravish\\Art\\Photos")

    def open_fuzz_baby():
        """Open fuzz baby directory"""
        actions.user.run("F:\\fuzzbaby\\")

    def get_talon_user_directory() -> str:
        """Get Talon user directory path"""
        return f"C:\\Users\\{settings.get('user.user')}\\AppData\\Roaming\\talon\\user"
