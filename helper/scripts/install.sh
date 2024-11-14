#!/bin/bash
chmod +x *.sh
cp -rfv ../config/* /etc/
./python-install.sh
./python3-replace.sh
./update-alt.sh
./pip-install.sh
./neo-install.sh
