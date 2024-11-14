#!/bin/bash

sudo apt -y update
sudo apt install -y python3-apt
sudo apt install -y software-properties-common

echo -e '\n' | sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt -y update
