
print_help (){
  echo "Install and configure the dotfiles for Arch Linux Ricing"
  echo "Usage: $0 [-a] [-i] [-c] [-o <only>]"
  echo "  -a: Install and configure everything"
  echo "  -i: Install only"
  echo "  -c: Configure only"
  echo "  -o: Install only the specified package"
  echo "  -h: Print this help"
}

while getopts "haico:" opt; do
  case "$opt" in
    h) print_help; exit 0 ;;
    a) action=ALL ;;
    i) action=INSTALL ;;
    c) action=CONFIGURE ;;
    o) only=$OPTARG ;;
  esac
done

if [ -z "$action" ]; then
  action=ALL
fi

case $action in
  ALL)
    ./installer.sh
    ./configure.sh
    ;;
  INSTALL)
    if [ -n "$only" ]; then
      ./installer.sh -o $only
    else
      ./installer.sh
    fi
    ;;
  CONFIGURE)
    ./configure.sh
    ;;
esac