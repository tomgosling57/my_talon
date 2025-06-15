# photoshop.talon
app: Adobe Photoshop 2025
-
keyboard shortcuts: key("alt-ctrl-shift-k")


# Tools settings
brush size: user.grid_win_click("7764")
brush opacity: user.photoshop_brush_opacity()

# Tools
brush tool: user.brush_tool()
marque tool: user.marque_tool()
move tool: user.move_tool()
lasso tool: user.lasso_tool()
bucket tool: user.bucket_tool()
zoom tool: user.zoom_tool()
erase tool: user.erase_tool()
rectangle tool: user.rectangle_tool()

# Layers
new layer: key(ctrl-shift-n)
duplicate layer: key(ctrl-j)
liquify: key(ctrl-alt-shift-l)
invert: key(ctrl-i)
desaturate: key(ctrl-shift-u)
hover layers: user.hover_layers()
layer via copy: key("ctrl-j")
layer via cut: key("ctrl-shift-j")
export as PNG: key("shift-ctrl-'")
select blending mode: user.grid_win_click("6228")
layer fill: user.photoshop_fill()
opacity: user.grid_win_click("6328")


# Panels
toggle layers panel: key("f7")
toggle history panel: key("f10")

# Zoom
zoom in: key(ctrl-plus)
zoom out: key(ctrl-minus)

# File
save as: key(ctrl-shift-s)
save: key(ctrl-s)
open: key(ctrl-o)
close: key(ctrl-w)
quit: key(ctrl-q)
export: key(ctrl-alt-shift-s)

# Dropdowns
edit: user.photoshop_edit()
file: user.photoshop_file()
image: user.photoshop_image()
layer: user.photoshop_layer()
view: user.photoshop_view()
window: user.photoshop_window()
filter: user.photoshop_filter()
select: user.photoshop_select()
type: user.photoshop_type()
filter layers: user.photoshop_filter_layers()

# Transform
transform: key(ctrl-t)
transform width: user.photoshop_transform_width()
transform height: user.photoshop_transform_height()
transform link: user.grid_n_click("7869")
transform x: user.photoshop_transform_x()
transform y: user.photoshop_transform_y()
transform angle: user.photoshop_transform_angle()
transform layer x: user.photoshop_transform_layer_x()
transform layer y: user.photoshop_transform_layer_y()
transform layer width: user.photoshop_transform_layer_width()
transform layer height: user.photoshop_transform_layer_height()
centre x: user.photoshop_center_x()
center y: user.photoshop_center_y()
fit screen: key(ctrl-0)
actual pixels: key(ctrl-alt-0)

# Blending Modes
normal blend: key("v shift-alt-n")
dissolve blend: key("v shift-alt-i")
darken blend: key("v shift-alt-k")
multiply blend: key("v shift-alt-m")
color burn blend: key("v shift-alt-b")
linear burn blend: key("v shift-alt-a")
lighten blend: key("v shift-alt-g")
screen blend: key("v shift-alt-s")
color dodge blend: key("v shift-alt-d")
linear dodge blend: key("v shift-alt-w")
overlay blend: key("v shift-alt-o")
soft light blend: key("v shift-alt-f")
hard light blend: key("v shift-alt-h")
vivid light blend: key("v shift-alt-v")
linear light blend: key("v shift-alt-j")
pin light blend: key("v shift-alt-z")
hard mix blend: key("v shift-alt-l")
difference blend: key("v shift-alt-e")
exclusion blend: key("v shift-alt-x")
hue blend: key("v shift-alt-u")
saturation blend: key("v shift-alt-t")
color blend: key("v shift-alt-c")
luminosity blend: key("v shift-alt-y")

# Adjustments
brightness contrast: key("shift-ctrl-1")
levels: key("ctrl-l")
curves: key("ctrl-m")
exposure: key("shift-f1")
hue saturation: key("ctrl-u")
color balance: key("ctrl-b")
invert: key("ctrl-i")
threshold: key("ctrl-f3")
desaturate: key("shift-ctrl-u")
auto tone: key("shift-ctrl-l")
auto contrast: key("alt-shift-ctrl-l")
auto color: key("shift-ctrl-b")
image size: key("alt-ctrl-i")
canvas size: key("alt-ctrl-c")
rotate one eighty: key("alt-f3")
rotate ninety clockwise: key("alt-f5")
rotate ninety counterclockwise: key("alt-f6")
