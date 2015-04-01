#!/bin/bash
#Installs Python 2.7.9 on a Centos6.6 fresh install 

ifup eth0
iptables -F
yum update -y
yum groupinstall -y 'development tools'
yum install -y zlib-devel bzip2-devel openssl-devel xz-libs wget sqlite-devel
wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz
xz -d Python-2.7.9.tar.xz
tar -xvf Python-2.7.9.tar
cd Python-2.7.9
./configure --prefix=/usr/local
make
make altinstall
export PATH="/usr/local/bin:$PATH"
curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | python2.7 -
pip2.7 install django

#Remember to use python2.7 e pip2.7 to install and run django commands, or make alias for them
