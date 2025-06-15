tag: user.roo
-
next mode: key("ctrl-.")
[select | set ] profile: user.roo_select_profile()
edit profile: user.roo_edit_profile()

roo settings: user.roo_settings()

auto approvals: 
    user.grid_win("1724")
    mouse_click()
open approvals:
    user.grid_win("182")    
    mouse_click()

ask roo:
    user.grid_win("1")
    mouse_click()

roo run: user.grid_n_click("1811")
run command: user.grid_n_click("1811")

close task:
    user.grid_win("8713")
    mouse_click()

done: 
    user.disable_tag("roo_settings")
    user.grid_win_click("8712")

modes:user.roo_modes()
edit mode: user.roo_edit_mode()
new task: user.vscode("roo-cline.newTask")

enhance prompt: user.grid_n_click("1344")()