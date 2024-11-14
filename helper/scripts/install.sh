#!/bin/bash
chmod +x *.sh
cp -rfv ../config/* /etc/
./python3-install.sh
./python3-replace.sh
./update-alt.sh

