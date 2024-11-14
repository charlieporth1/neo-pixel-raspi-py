#!/bin/bash
chmod +x *.sh
cp -rfv ../config/* /etc/
./add-ppa.sh
./python3-install.sh
./python3-replace.sh
./update-alt.sh
./neo-install.sh
