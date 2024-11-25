#!/bin/bash
chmod +x *.sh
wget -O deadsnakes-ubuntu-ppa.gpg https://keyserver.ubuntu.com/pks/pool/archive/key/F23C5A6CF475977595C89F51BA6932366A755776
sudo gpg --keyserver hkps://keyserver.ubuntu.com:443 --import deadsnakes-ubuntu-ppa.gpg
cp -rfv ../config/* /etc/
./python-install.sh
./python3-replace.sh
./update-alt.sh
./pip-install.sh
./neo-install.sh
