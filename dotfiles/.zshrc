export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="bira"

plugins=(git node docker)

source $ZSH/oh-my-zsh.sh

export PATH="$PATH:/$HOME/.local/bin"

alias dcu="docker compose up"
alias dcd="docker compose down"
alias dcr="docker compose run"
alias dob="docker build"

# export NVM_DIR="$HOME/.nvm"
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
# [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Check if docker service is running
# IS_DOCKER_RUNNING="$(service docker status | grep 'Docker is running')"
# if [[ -z $IS_DOCKER_RUNNING ]]; then
#   printf "Starting docker ...\n"
#   sudo /usr/sbin/service docker start
# fi

wal -R -q && clear