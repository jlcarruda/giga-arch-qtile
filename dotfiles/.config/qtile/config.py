# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# import os
import subprocess
from .theme import *
from .helpers import *
from .variables import *
from .layout import *
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy


# # Get current screen resolution
# resolution = os.popen('xdpyinfo | awk "/dimensions/{print $2}"').read()
# xres = resolution[17:21]
# yres = resolution[22:26]

# home = os.path.expanduser('~')
# terminal = "alacritty"

# ## THEME VARIABLES
# theme_list = []
# current_theme = os.getenv("GIGA_THEME") or "giga"
# main_font = "Fira Code Medium" # Font in use for the entire system
# awesome_font = "Font Awesome 6 Pro" # Font for the icons
# bar_position = "top" # Bar position (top or bottom)

# # Set Ethernet or Wifi icon according
# if get_net_dev().startswith('e'):
#   wifi_icon=''
# else:
#   wifi_icon=''

# ## WALLPAPER THEME
# wp_theme="nord"

# ## Openwather
# app_id="f62be80381868d842c7a8bc4aaf93f0d"

# ## QTILE VARIABLES 
# mod = "mod4"
# alt = "mod1"
# hide_unused_groups=True # Unused groups visibility
# dgroups_key_binder = None
# dgroups_app_rules = []  # type: list
# follow_mouse_focus = True
# bring_front_click = False
# floats_kept_above = True
# cursor_warp = False
# prompt = "".format(os.getenv("USER"), socket.gethostname()) # Format of the prompt

# ## NETWORK
# private_ip = get_private_ip()
# public_ip = get_public_ip()


# mod = "mod4"
# alt = "mod1"
# terminal = "alacritty"

# home = os.path.expanduser('~') # Path for use in folders

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([alt], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([alt], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([alt], "j", lazy.layout.down(), desc="Move focus down"),
    Key([alt], "k", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([alt, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([alt, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([alt, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([alt, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([alt, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([alt, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([alt, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([alt, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([alt], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([alt], "t", lazy.spawn(terminal), desc="Launch terminal"),
    # ROFI HKs
    Key([mod, "shift"], "Return", lazy.spawn('rofi -show drun -show-icons -theme "~/.config/rofi/launcher.rasi"')), # Open Rofi launcher
    Key([alt, "shift"], "Return", lazy.spawn('sudo rofi -show drun -show-icons -theme "~/.config/rofi/launcher.rasi"')), # Open Rofi launcher as Sudo
    Key([mod, "shift"], "q",lazy.shutdown()), # Logout         
]

#groups = [Group(i) for i in "123456789"]
groups = []
#### Groups Labels
group_labels=["零","一","二","三","四","五","六","七","八","九"] # Kanji Numbers
#group_labels=["0","1","2","3","4","5","6","7","8","9"] # Numbers
#group_labels=["","","","","","","","","",""] # Circles
#group_labels=["","","","","","","","","",""] # Dot Circles
# group_labels=["","","","","","","","","",""] # Custom
#group_labels=["","","","","","","","","",""] # Star Wars

group_names = ["1","2","3","4","5","6","7","8","9","0"]
group_layouts=["monadtall", "monadtall", "monadtall", "monadtall","monadtall", "monadtall", "monadtall","monadwide", "monadtall", "monadtall"]

layouts = init_layouts()

for i in range(len(group_names)):
  groups.append(
    Group(
      name=group_names[i],
      layout=group_layouts[i].lower(),
      label=group_labels[i],
  ))


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

## Hooks
@hook.subscribe.startup # This file gets executed everytime qtile restarts
def start():
  subprocess.call('/usr/bin/boot')
      
@hook.subscribe.startup_once # Ths file gets executed at first start only
def start_once():
  subprocess.call('/usr/bin/autostart')

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

def wlan_widgets():
    return [
         widget.Wlan(
            decorations=[RectDecoration(
                use_widget_background=True, radius=0, padding_y=1, filled=True)],
            background=secondary_color[0],
            fontsize=font_size,
            interface=net_interface,
            format='{essid}',
            disconnected_message='',
            foreground=color[3],
            width=widget_width,
            scroll=True,
            scroll_repeat=True,
            scroll_interval=0.1,
            scroll_step=1,
            update_interval=1,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(home + "/.local/bin/wifi2")}),
        widget.Wlan(
            decorations=[RectDecoration(
                use_widget_background=True, radius=0, padding_y=1, filled=True)],
            background=secondary_color[0],
            fontsize=font_size,
            interface=net_interface,
            format='{percent:2.0%}',
            disconnected_message='',
            foreground=color[3],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_function(network_widget)}
        ),
    ]


def net_widgets():
    return [
        widget.WidgetBox(
            decorations=[RectDecoration(use_widget_background=True, radius=[
                                        10, 0, 0, 10], padding_y=1, filled=True)],
            background=secondary_color[0],
            fontsize=font_size-2,
            text_closed=' ' + wifi_icon + ' ',
            text_open='  ',
            foreground=color[3],
            widgets=[
                widget.TextBox(
                    decorations=[RectDecoration(
                      use_widget_background=True, radius=0, padding_y=1, filled=True)],
                    background=secondary_color[0],
                    fontsize=font_size-2,
                    text='  ',
                    foreground=color[4],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(home + "/.local/bin/wifi2")}),
                widget.TextBox(
                    decorations=[RectDecoration(
                        use_widget_background=True, radius=0, padding_y=1, filled=True)],
                    background=secondary_color[0],
                    fontsize=font_size,
                    text=private_ip,
                    foreground=secondary_color[7],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(home + "/.local/bin/wifi2")}),
                widget.TextBox(
                    decorations=[RectDecoration(
                        use_widget_background=True, radius=0, padding_y=1, filled=True)],
                    background=secondary_color[0],
                    fontsize=font_size-2,
                    text='  ',
                    foreground=color[4],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(home + "/.local/bin/wifi2")}),
                widget.TextBox(
                    decorations=[RectDecoration(
                        use_widget_background=True, radius=0, padding_y=1, filled=True)],
                    background=secondary_color[0],
                    fontsize=font_size,
                    text=public_ip,
                    foreground=secondary_color[7],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(home + "/.local/bin/wifi2")}),
                widget.TextBox(
                    decorations=[RectDecoration(
                        use_widget_background=True, radius=0, padding_y=1, filled=True)],
                    background=secondary_color[0],
                    fontsize=font_size-2,
                    text=wifi_icon,
                    foreground=color[4],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(home + "/.local/bin/wifi2")}),
            ]
        ),
       *wlan_widgets(),
        widget.Net(
            decorations=[RectDecoration(use_widget_background=True, radius=[
                0, 10, 10, 0], padding_y=1, filled=True)],
            background=secondary_color[0],
            fontsize=font_size,
            prefix='M',
            interface=net_interface,
            format='{interface}{down}↓↑{up} - {total}',
            foreground=secondary_color[7],
            use_bits=True,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_function(network_widget)},
        ),
    ]


def groupbox_widgets():
    return [
        widget.TextBox(
            foreground=secondary_color[1],
            text=" ",
            fontsize=font_size,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_function(session_widget)}
        ),
        extra_widget.CurrentLayoutIcon(
            foreground=secondary_color[1],
        ),
        widget.Spacer(
            length=5,
            background=transparent,
        ),
        widget.GroupBox(
            font=awesome_font,
            background=secondary_color[0],
            fontsize=font_size,
            disable_drag=True,
            hide_unused=hide_unused_groups,
            borderwidth=0,
            active=color[2],  # Program opened in that group
            inactive=color[5],  # Empty Group
            rounded=False,
            highlight_method="text",
            this_current_screen_border=color[0],
            center_aligned=True,
            other_curren_screen_border=color[0],
            block_highlight_text_color=color[0],
            urgent_border="fc0000",
            decorations=[RectDecoration(
                use_widget_background=True, radius=10, padding_y=1, filled=True)],
        ),
    ]


def init_widget_list():
    groupbox_widgets_list = groupbox_widgets()
    net_widgets_list = net_widgets()
    widgets = [
        *groupbox_widgets_list,
        widget.Spacer(
            length=5,
            background=transparent,
        ),
        widget.Prompt(
            prompt=prompt,
            fontsize=font_size,
            foreground=color[4],
            cursor_color=color[4],
            visual_bell_color=[4],
            visual_bell_time=0.2,
        ),
        widget.Spacer(
            length=20,
            background=transparent,
        ),
        widget.Mpris2(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                terminal + " -e cava")},
            objname=None,
            fontsize=font_size,
            foreground=color[5],
            width=widget_width,
            format='{xesam:artist}  {xesam:title}',
            stopped_text="Stop",
            paused_text='  ',
            scroll=True,
            scroll_repeat=True,
            scroll_delay=0.1,
        ),
        widget.Spacer(
            background=transparent,
        ),
        widget.TextBox(
            foreground=color[2],
            text="",
            fontsize=font_size-2,
            mouse_callbacks={'Button1': lambda: qtile.cmd_function(calendar_notification), 'Button4': lambda: qtile.cmd_function(
                calendar_notification_prev), 'Button5': lambda: qtile.cmd_function(calendar_notification_next)},
        ),
        widget.Clock(
            foreground=secondary_color[7],
            fontsize=font_size - 2,
            format="%H:%M",
            update_interval=1,
            mouse_callbacks={'Button1': lambda: qtile.cmd_function(calendar_notification), 'Button4': lambda: qtile.cmd_function(
                calendar_notification_prev), 'Button5': lambda: qtile.cmd_function(calendar_notification_next)},
        ),
        widget.Spacer(
            length=bar.STRETCH,
            background=transparent,
        ),
        widget.TextBox(
            decorations=[RectDecoration(use_widget_background=True, radius=[
                                        10, 0, 0, 10], padding_y=1, filled=True)],
            background=secondary_color[0],
            foreground=color[3],
            text=" ",
            fontsize=font_size-2,
        ),
        widget.CPU(
            decorations=[RectDecoration(use_widget_background=True, radius=[
                                        0, 10, 10, 0], padding_y=1, filled=True)],
            background=secondary_color[0],
            foreground=secondary_color[7],
            format='{load_percent}% ',
            fontsize=font_size,
        ),
        widget.Spacer(
            length=5,
            background=transparent,
        ),
        widget.TextBox(
            decorations=[RectDecoration(use_widget_background=True, radius=[
                                        10, 0, 0, 10], padding_y=1, filled=True)],
            background=secondary_color[0],
            fontsize=font_size-2,
            foreground=color[4],
            text=" ",
        ),
        widget.Memory(
            decorations=[RectDecoration(use_widget_background=True, radius=[
                                        0, 10, 10, 0], padding_y=1, filled=True)],
            background=secondary_color[0],
            foreground=secondary_color[7],
            format='{MemUsed:.0f}{mm} ',
            measure_mem='M',
            fontsize=font_size,
        ),
        widget.Spacer(
            length=5,
            background=transparent,
        ),
        widget.TextBox(
            decorations=[RectDecoration(use_widget_background=True, radius=[
                                        10, 0, 0, 10], padding_y=1, filled=True)],
            background=secondary_color[0],
            text="",
            foreground=color[5],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol'), 'Button4': lambda: qtile.cmd_spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)",
                                                                                                                   shell=True), 'Button5': lambda: qtile.cmd_spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
            fontsize=font_size-2
        ),
        extra_widget.ALSAWidget(
            decorations=[RectDecoration(
                use_widget_background=True, radius=0, padding_y=1, filled=True)],
            background=secondary_color[0],
            device='Master',
            bar_colour_high=color[5],
            bar_colour_loud=color[5],
            bar_colour_normal=color[5],
            bar_colour_mute=color[5],
            hide_interval=5,
            update_interval=0.1,
            bar_width=80,
            mode='bar',
            text_format=' ',
        ),
        widget.TextBox(
            decorations=[RectDecoration(colour=secondary_color[0], radius=[
                                        0, 10, 10, 0], padding_y=1, filled=True)],
            text=" ",
            foreground=color[5],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol'), 'Button4': lambda: qtile.cmd_spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)",
                                                                                                                   shell=True), 'Button5': lambda: qtile.cmd_spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
            fontsize=font_size-2
        ),
        widget.Spacer(
            length=5,
            background=transparent,
        ),
        *net_widgets_list,
        widget.Spacer(
            length=5,
            background=transparent,
        ),
    ]
    return widgets


bar_config = {
    "widgets": init_widget_list(),
    "size": bar_size,
    "background": color[0],
    "margin": bar_margin
}


def screen1_widgets():
    return init_widget_list()

def init_screens_bottom():
    return [Screen(bottom=bar.Bar(**bar_config))]


def init_screens_top():
    return [Screen(top=bar.Bar(**bar_config))]

widgets_screen1 = screen1_widgets()

# if bar_position == "top":
screens = init_screens_top()
# else:

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
