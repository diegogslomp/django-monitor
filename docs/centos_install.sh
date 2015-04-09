#!/bin/bash
#Installs pyenv on a Centos

yum update -y
yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel git

curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile

pyenv install 3.4.3
pyenv global 3.4.3
pip install django

# Reboot or type `source ~/.bash_profile` for every shell opened until reboot.
