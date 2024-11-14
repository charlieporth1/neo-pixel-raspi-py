#!/bin/bash

cd /tmp/

sudo apt download python3.7
sudo apt download python3.7-dev

sudo dpkg -i *.deb
