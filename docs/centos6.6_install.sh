#!/bin/bash
#Installs pyenv on a Centos6.6 fresh install 

sudo ifup eth0
sudo iptables -F
sudo yum update -y
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install 3.4.3
pyenv global 3.4.3

# Reboot to don't type `source ~/.bash_profile` for every shell opened
