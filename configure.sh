function set_fonts()
{
  mkdir -p $HOME/.fonts
  cp -a ./dotfiles/.fonts/. $HOME/.fonts
  sudo mkdir -p /usr/share/fonts/OTF
  sudo mkdir -p /usr/share/fonts/TTF
  sudo cp ./dotfiles/.fonts/*.ttf /usr/share/fonts/TTF
  sudo cp ./dotfiles/.fonts/*.otf /usr/share/fonts/OTF
  fc-cache -f -v
}

function lightdm_configure()
{
  sudo cp ./dotfiles/lightdm/lightdm.conf /etc/lightdm/lightdm.conf
  sudo cp ./dotfiles/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/lightdm-gtk-greeter.conf
  sudo cp ./dotfiles/lightdm/lightdmxrandr.sh /usr/share
}

function copy_wallpapers()
{
  mkdir -p $HOME/Pictures/Wallpapers
  sudo mkdir -p /usr/local/backgrounds
  sudo cp ./Wallpapers/background.png /usr/local/backgrounds
  cp -r ./Wallpapers/* $HOME/Pictures/Wallpapers
}

function configure()
{
  cp -a $HOME/.ricing/dotfiles/.config/. $HOME/.config/
  cp $HOME/.ricing/dotfiles/.local/bin/autostart /usr/bin
  cp $HOME/.ricing/dotfiles/.local/bin/boot /usr/bin
  cp $HOME/.ricing/dotfiles/.local/bin/genwal /usr/bin
  cp $HOME/.ricing/dotfiles/.local/bin/selectwal /usr/bin
  cp $HOME/.ricing/dotfiles/.local/bin/wifi2 /usr/bin
  cp $HOME/.ricing/dotfiles/.zshrc $HOME
  cp $HOME/.ricing/dotfiles/.xinitrc $HOME
  cp $HOME/.ricing/dotfiles/.xprofile $HOME
  cp $HOME/.ricing/dotfiles/.profile $HOME
}

configure
set_fonts
lightdm_configure