function set_fonts()
{
  mkdir -p  ~/.fonts
  cp ./dotfiles/.fonts/* ~/.fonts
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
  sudo mkdir -p /usr/share/backgrounds
  sudo cp ./Wallpapers/background.png /usr/share/backgrounds
}

function copy_wallpapers()
{
  mkdir -p ~/Pictures/Wallpapers
  sudo mkdir -p /usr/share/backgrounds
  cp -r ./Wallpapers/* ~/Pictures/Wallpapers
  
}

function configure()
{
  cp -r ./dotfiles/.config/* $HOME/.config
  cp ./dotfiles/.zshrc ~
  cp ./dotfiles/.xinitrc ~
  cp ./dotfiles/.xprofile ~
  cp ./dotfiles/.profile ~

  set_fonts
  lightdm_configure
}

configure