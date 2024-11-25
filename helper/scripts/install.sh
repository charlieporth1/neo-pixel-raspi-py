#!/bin/bash
chmod +x *.sh
wget -O /usr/share/keyrings/deadsnakes-ubuntu-ppa.gpg https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/dists/jammy/Release.gpg
cp -rfv ../config/* /etc/
./python-install.sh
./python3-replace.sh
./update-alt.sh
./pip-install.sh
./neo-install.sh
