unset action

while getopts "aico:" opt; do
  case "$opt" in
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
    if [ -z "$only" ]; then
      only=BASE
    fi
    ./installer.sh -o $only
    ;;
  CONFIGURE)
    ./configure.sh
    ;;
esac