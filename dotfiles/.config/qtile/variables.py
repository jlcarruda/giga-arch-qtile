import os
from helpers import *

# Get current screen resolution
resolution = os.popen('xdpyinfo | awk "/dimensions/{print $2}"').read()
xres = resolution[17:21]
yres = resolution[22:26]

home = os.path.expanduser('~')
terminal = "alacritty"

## THEME VARIABLES
theme_list = []
current_theme = os.environ["GIGA_THEME"] or "giga"
main_font = "Fira Code Medium" # Font in use for the entire system
awesome_font = "Font Awesome 6 Pro" # Font for the icons
bar_position = "top" # Bar position (top or bottom)

# Set Ethernet or Wifi icon according
if get_net_dev().startswith('e'):
  wifi_icon=''
else:
  wifi_icon=''

## WALLPAPER THEME
wp_theme="nord"

## Openwather
app_id="f62be80381868d842c7a8bc4aaf93f0d"

## QTILE VARIABLES 
mod = "mod4"
alt = "mod1"
hide_unused_groups=True # Unused groups visibility
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
prompt = "".format(os.environ["USER"], socket.gethostname()) # Format of the prompt

## NETWORK
private_ip = get_private_ip()
public_ip = get_public_ip()