app: vscode
-
bar docker: user.vscode("dockerContainers.focus")    
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
pallete: key("ctrl-shift-p")

docker up: user.run_command("docker compose up -d")
docker down: user.run_command("docker compose down")
docker build: user.run_command("docker build .")
docker remove all: user.run_command("docker rmi $(docker images -q) -f")
docker shell: user.vscode("vscode-docker.containers.attachShell")

prisma generate: user.run_command("npx prisma generate")
prisma migrate dev: user.run_command("npx prisma migrate dev")
prisma pull: user.run_command("npx prisma db pull")
prisma push: user.run_command("npx prisma db push")

runup: user.run_command("npm run dev")
install: user.run_command("npm install")

git init: user.run_command("git init")
git clone: insert("git clone ")
git add: insert("git add ")
git commit: insert("git commit -m ")
git remote add: insert("git remote add ")
git remote add origin main: insert("git remote add origin/main ")
git pool: insert("git pull ")
git push: insert("git push ")
git reset: insert("git reset ")
git checkout: insert("git checkout ")
git branch: insert("git branch ")
