PWD=$(pwd)

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

function config_and_dotlocal()
{
  cp -a $PWD/dotfiles/.config/. $HOME/.config/
  sudo cp $PWD/dotfiles/.local/bin/autostart /usr/bin
  sudo cp $PWD/dotfiles/.local/bin/boot /usr/bin
  sudo cp $PWD/dotfiles/.local/bin/genwal /usr/bin
  sudo cp $PWD/dotfiles/.local/bin/selectwal /usr/bin
  sudo cp $PWD/dotfiles/.local/bin/wifi2 /usr/bin
}

function omzsh_install() {
  if [ "$(command -v zsh)" ]; then
    echo "===> ZSH is already installed. Moving foward..."
    return
  else
    echo "===> Installing Zsh..."
    sudo pacman -S zsh --noconfirm
  fi
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
}

function copy_dotfiles() {
  cp $PWD/dotfiles/.zshrc $HOME
  cp $PWD/dotfiles/.xinitrc $HOME
  cp $PWD/dotfiles/.xprofile $HOME
  cp $PWD/dotfiles/.profile $HOME
}

config_and_dotlocal
set_fonts
copy_wallpapers
lightdm_configure

wal -i /usr/local/backgrounds/background.png
wpg-install.sh -gio
omzsh_install
copy_dotfiles
genwal
