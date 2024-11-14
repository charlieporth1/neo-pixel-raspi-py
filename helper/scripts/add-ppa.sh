#!/bin/bash

sudo apt -y update
sudo apt install -y python3-apt

echo -e '\n' | sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt -y update
