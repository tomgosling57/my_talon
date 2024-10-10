from talon import Context, Module, actions, clip, imgui, speech_system
import json, os

mod = Module()

mod.list(
    "saved_macros",
    desc="list of macros that have been saved with the 'macro save' command",
)
ctx = Context()
ctx.matches = """
os: windows
"""

macros = {}
macro = []
recording = False
macros_file = os.path.join(os.getcwd(), "user", "my_talon", "macro", "macros.json")

@imgui.open(y=0)
def macro_list_gui(gui: imgui.GUI):
    gui.text("macros")
    gui.line()
    for command_name in macros.keys():
        gui.text(command_name)

    if gui.button("macro list close"):
        actions.user.macro_list_close()


@mod.action_class
class Actions:
    def macro_record():
        """Begin recording a new voice command macro."""
        global macro
        global recording

        macro = []
        recording = True

    def macro_stop():
        """Stop recording the macro."""
        global recording
        if recording and len(macro) != 0:
            # Remove the final `macro stop`/`macro play`/`macro save` command
            macro.pop()
        recording = False

    def macro_save(name: str):
        """Save the macro."""
        actions.user.macro_stop()
        macros[name] = macro

        ctx.lists["user.saved_macros"] = macros.keys()

    def macro_remove(name: str):
        """Remove the macro."""
        actions.user.macro_stop()
        del macros[name]
        ctx.lists["user.saved_macros"] = macros.keys()

    def macro_list():
        """List all saved macros."""
        macro_list_gui.show()

    def macro_list_close():
        """Close the saved macros list."""
        macro_list_gui.hide()

    def macro_play(name: str):
        """Execute the commands in the last recorded macro."""
        actions.user.macro_stop()

        selected_macro = macro
        if name in macros:
            selected_macro = macros[name]

        for words in selected_macro:
            print(words)
            actions.mimic(words)

    def macro_copy(name: str):
        """Copy the specified macro to the clipboard as a Talon command."""
        selected_macro = macro

        if not name:
            # No macro name was provided, so we'll copy the most recent command
            # with this default name
            name = "last macro command"
        elif name in macros:
            selected_macro = macros[name]

        l = [name + ":"]

        for words in selected_macro:
            l.append(f'\tmimic("{" ".join(words)}")')

        clip.set_text("\n".join(l))

    def macro_append_command(words: list[str]):
        """Append a command to the current macro; called when a voice command is uttered while recording a macro."""
        assert recording, "Not currently recording a macro"
        macro.append(words)

    def macro_dump():
        """Dump the macros to a JSON file."""
        global macros
        with open(macros_file, "w") as f:
            json.dump(macros, f, indent=4)
        actions.user.macro_list()

    def macro_load():
        """Load the macros from a JSON file, create the file if it doesn't exist."""
        global macros
        if os.path.exists(macros_file):
            # Load the existing macros from the JSON file
            with open(macros_file, "r") as f:
                macros = json.load(f)
            ctx.lists["user.saved_macros"] = macros.keys()
        else:
            # File does not exist, so create an empty file and initialize macros
            with open(macros_file, "w") as f:
                json.dump({}, f, indent=4)  # Write an empty dictionary to the file
            macros = {}  # Initialize an empty macros dictionary
            print("No existing macro file found. Created a new one.")

def fn(d):
    if not recording or "parsed" not in d:
        return
    actions.user.macro_append_command(d["parsed"]._unmapped)

speech_system.register("pre:phrase", fn)
