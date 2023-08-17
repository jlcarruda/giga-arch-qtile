import os
import json
from libqtile import layout

# Get current screen resolution
resolution = os.popen('xdpyinfo | awk "/dimensions/{print $2}"').read()
xres = resolution[17:21]
yres = resolution[22:26]

main_font = "Fira Code Medium" # Font in use for the entire system
awesome_font = "Font Awesome 6 Pro" # Font for the icons
bar_position = "top" # Bar position (top or bottom)
home = os.path.expanduser('~')

## Import Colors from Pywal
with open(home + '/.cache/wal/colors.json') as wal_import:
  data = json.load(wal_import)
  wallpaper = data['wallpaper']
  colors = data['colors']
  val_colors = list(colors.values())
  def getList(val_colors):
    return [*val_colors]
    
  def init_colors():
    return [*val_colors]

color = init_colors()

## Generate Secondary Palette
def secondary_pallete(colors, differentiator):
    updated_colors = []
    for color in colors:
        # Remove the '#' symbol
        color = color.lstrip('#')

        # Convert hexadecimal colors to integers
        color_int = int(color, 16)
        differentiator_int = int(differentiator, 16)

        # Perform addition
        result_int = color_int + differentiator_int

        # Ensure the result is within the valid range of 0-FFFFFF
        result_int = min(result_int, 0xFFFFFF)
        result_int = max(result_int, 0)

        # Convert the result back to hexadecimal
        result_hex = '#' + hex(result_int)[2:].zfill(6).upper()

        updated_colors.append(result_hex)

    return updated_colors

secondary_color = secondary_pallete(color, "0x222222")

# Set Bar and font sizes for different resolutions
if xres >= "3840" and yres >= "2160": #4k
  layout_margin=15
  single_layout_margin=10  
  layout_border_width=5
  single_border_width=5
  font_size=20
  bar_size=30
  widget_width=400
  max_ratio=0.85
  ratio=0.70
  if bar_position == "bottom":
    bar_margin=[0,15,10,15]
  else:
    bar_margin=[10,15,0,15]
elif xres == "1920" and yres == "1080": #FullHD
  layout_margin=10
  single_layout_margin=5  
  layout_border_width=4 
  single_border_width=4
  font_size=16
  bar_size=25
  widget_width=220
  max_ratio=0.85
  ratio=0.70
  if bar_position == "bottom":
    bar_margin=[0,10,5,10]
  else:
    bar_margin=[5,10,0,10]
else: # 1366 x 768 Macbook air 11"
  layout_margin=2
  single_layout_margin=2  
  layout_border_width=2
  single_border_width=2
  font_size=13
  bar_size=20
  widget_width=100
  max_ratio=0.60
  ratio=0.50
  bar_margin=[0,0,0,0]


## Layouts
def init_layout_theme():
  return {"font":main_font,
    "fontsize":font_size,
    "margin":layout_margin,
    "border_on_single":False,
    "border_width":layout_border_width,
    "border_normal":color[0],
    "border_focus":color[2],
    "single_margin":single_layout_margin,
    "single_border_width":single_border_width,
    "change_ratio":0.01,
    "new_client_position":'bottom',
    }

layout_theme=init_layout_theme()

def init_layouts():
  return [
    layout.Spiral(main_pane="left",ratio_increment=0.01,**layout_theme),
    layout.MonadTall(max_ratio=max_ratio,ratio=ratio,**layout_theme),
    layout.MonadWide(max_ratio=0.85,ratio=0.85,**layout_theme),
    layout.Floating(**layout_theme),
    ]
