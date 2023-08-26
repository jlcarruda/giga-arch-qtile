#!/usr/bin/env bash

## Variables
BASE_PACKAGES="base_packages"
AUR_PACKAGES_FILE="aur_packages"
PIP_PACKAGES_FILE="pip_packages"

while getopts "o:" opt; do
  case "$opt" in
    o) only=$OPTARG ;;
  esac
done

function install_base_packages()
{
  sudo pacman -Syu --noconfirm
  echo "::::: Installing base packages :::::"
  while read -r package; do
      sudo pacman -S --noconfirm "$package"
  done < "$BASE_PACKAGES"

  echo ":::"
  echo "Instalation complete!"
}

function paru_install()
{
  if [ "$(command -v paru)" ]; then
    echo "===> PARU is already installed. Moving foward..."
    return
  fi
  echo "::::: Installing paru AUR helper :::::"
  git clone https://aur.archlinux.org/paru.git 
  cd paru
  makepkg -si --noconfirm
  cd ..
  rm -rf paru
}

function install_aur_packages()
{
  echo "::::: Installing AUR Packages :::::"
  while read -r package; do
    echo "Installing AUR package ${package}..."
    paru -S --noconfirm "$package"
  done < "$AUR_PACKAGES_FILE"

  echo ":::"
  echo "Instalation complete!"
}

function install_pip_packages()
{ 
  pip install -r "$PIP_PACKAGES_FILE" --break-system-packages

  echo "::: "
  echo "Installation complete!"
}


function install()
{
  ./ascii.sh
  if [ -n "$only" ]; then
    case $only in
      BASE)
        install_base_packages
        ;;
      AUR)
        paru_install
        install_aur_packages
        ;;
      PIP)
        install_pip_packages
        ;;
    esac
  else
    install_base_packages
    paru_install
    install_aur_packages
    install_pip_packages
  fi
}

install