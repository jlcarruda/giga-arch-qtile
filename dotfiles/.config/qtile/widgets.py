import subprocess
from rofi import Rofi

from variables import *
from layout import *

# Rofi Configuration files
rofi_right = Rofi(rofi_args=['-theme', '~/.config/rofi/right.rasi'])
rofi_network= Rofi(rofi_args=['-theme', '~/.config/rofi/network.rasi'])
rofi_left= Rofi(rofi_args=['-theme', '~/.config/rofi/left.rasi'])
rofi_wallpaper=Rofi(rofi_args=(['rofi', '-show file-browser-extended', '-theme', '~/.config/rofi/sel_wal.rasi', '-file-browser-dir', '~/Pictures/Wallpapers', '-file-browser-stdout']))


# Network Widget
def network_widget(qtile):
  options = [' Wlan Manager','  Bandwith Monitor (CLI)', ' Network Manager (CLI)']
  index, key = rofi_network.select(" " + private_ip + " -" + "  " + public_ip, options)
  if key == -1:
    rofi_network.close()
  else:
    if index == 0:
      print("Wlan Manager")
      # qtile.cmd_spawn(home + '/.local/bin/wifi2')
    elif index==1:
      qtile.cmd_spawn(terminal + ' -e bmon')
    else:
      qtile.cmd_spawn(terminal + ' -e nmtui')

# Logout widget
def session_widget(qtile):
  options = [' Log Out', ' Reboot',' Poweroff',' Lock']
  index, key = rofi_left.select('  Session', options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      qtile.shutdown()
    elif index == 1:
      os.system('systemctl reboot')
    elif index == 2:
      os.system('systemctl poweroff')    
    else:
      qtile.cmd_function(i3lock_colors)

# Change Theme widget
def change_theme(qtile):
  options = theme_list
  index, key = rofi_left.select('  Theme -  ' + current_theme , options)
  theme = theme_list[index]
  if key == -1:
    rofi_left.close()
  elif theme == current_theme:
    return
  else:
    # subprocess.run('rm -rf ~/.config/qtile/theme.py', shell=True)
    # variables[0]=theme[index] + "\n"
    # new_theme=theme[index] + ".py"
    # subprocess.run(['cp', themes_dir + "/" + new_theme, home + '/.config/qtile/theme.py'])
    # with open(home + '/.config/qtile/variables', 'w') as file:
    #   file.writelines(variables)
    os.environ["GIGA_THEME"] = theme
    qtile.cmd_reload_config()
    subprocess.run(["notify-send","-a", " GIGA", " Theme: ", "%s" %theme_list[index]])

def i3lock_colors(_):
  subprocess.run(['i3lock', 
    '--ring-color={}'.format(secondary_color[0])+"DD",
    '--inside-color={}'.format(secondary_color[0])+"DD",
    '--line-color={}'.format(color[2]),
    '--separator-color={}'.format(color[4]),
    '--time-color={}'.format(color[2]),           
    '--date-color={}'.format(color[4]),
    '--insidever-color={}'.format(secondary_color[0])+"DD",
    '--ringver-color={}'.format(secondary_color[0])+"DD",
    '--verif-color={}'.format(color[5]),          
    '--verif-text=Checking',
    '--insidewrong-color={}'.format(secondary_color[0])+"DD",
    '--ringwrong-color={}'.format(secondary_color[0])+"DD",
    '--wrong-color={}'.format(color[1]),
    '--wrong-text=Wrong!',
    '--keyhl-color={}'.format(color[1]),         
    '--bshl-color={}'.format(color[6]),            
    '--clock',
    '--blur', '10',                 
    '--indicator',       
    '--time-str="%H:%M:%S"',   
    '--date-str="%A, %Y-%m-%d"',
    ])

# Call Calendar Notification

def calendar_notification(_):{
    # subprocess.call(home + '/.local/bin/calendar')
}

def calendar_notification_prev(_):{
    # subprocess.call([home + '/.local/bin/calendar', 'prev'])
}

def calendar_notification_next(_):{
    # subprocess.call([home + '/.local/bin/calendar', 'next'])
}
