app: vscode
-
bar cline: user.vscode("    
)
bar roo: 
    user.vscode("roo-cline.SidebarProvider.focus")    
    user.enable_tag("user.roo")
roo mode: user.toggle_tag("user.roo")
roo settings mode: user.toggle_tag("user.roo_settings")

set sidebar width: user.set_sidebar_width()

[focus] terminal | bash:
    user.grid_win("2")
    mouse_click()
set terminal height:
    user.grid_win("52")
    mouse_release()
set bash height: mimic("set terminal height")
set console height: mimic("set terminal height")

kill terminal:
    user.grid_win("63284")
    mouse_click()
kill bash: mimic("kill terminal")
kill console: mimic("kill terminal")