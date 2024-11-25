#!/bin/bash
chmod +x *.sh
curl -fsSL https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/dists/jammy/Release.gpg \
    | sudo gpg --dearmor -o /usr/share/keyrings/deadsnakes-ubuntu-ppa.gpg
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BA6932366A755776 
cp -rfv ../config/* /etc/
./python-install.sh
./python3-replace.sh
./update-alt.sh
./pip-install.sh
./neo-install.sh
