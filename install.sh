unset action

while getopts "aic" opt; do
  case "$opt" in
    a) action=ALL ;;
    i) action=INSTALL ;;
    c) action=CONFIGURE ;;
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
    ./installer.sh
    ;;
  CONFIGURE)
    ./configure.sh
    ;;
esac