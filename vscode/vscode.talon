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

kill terminal: user.vscode("workbench.action.terminal.kill")
kill bash: user.vscode("workbench.action.terminal.kill")
kill console: user.vscode("workbench.action.terminal.kill")

new terminal: key("ctrl-~")
new bash: key("ctrl-~")
new console: key("ctrl-~")

select [terminal] output: user.select_terminal_output()
edit [text]: user.grid_n_click("5")