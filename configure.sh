function set_fonts()
{
  mkdir -p  $HOME/.fonts
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
  sudo mkdir -p /usr/share/backgrounds
  sudo cp ./Wallpapers/background.png /usr/share/backgrounds
  cp -r ./Wallpapers/* $HOME/Pictures/Wallpapers
}

function configure()
{
  cp -a ./dotfiles/.config/. $HOME/.config/
  cp -a ./dotfiles/.local/bin/. /usr/bin/
  cp ./dotfiles/.zshrc $HOME
  cp ./dotfiles/.xinitrc $HOME
  cp ./dotfiles/.xprofile $HOME
  cp ./dotfiles/.profile $HOME
}

configure
set_fonts
lightdm_configure