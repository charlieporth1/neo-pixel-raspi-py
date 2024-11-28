#!/bin/bash
echo $PWD
cd $PWD

# needed
apt install -y scons cmake swig git
apt install -y build-essential
apt install -y git

# Py2 if old os
apt install -y python
apt install -y python-pip
apt install -y python-dev
apt install -y python-backports.ssl-match-hostname

# py3 install
apt install -y python3
apt install -y python3-full
apt install -y python3-dev
apt install -y python3-pip3

# 2 to 3 convesion
apt install -y python-is-python3
apt install -y 2to3
apt install -y python-dev-is-python3

# Lib install
apt install -y libffi-dev
apt install -y libzbar-dev
apt install -y libzbar0
apt install -y libcblas-dev
apt install -y libhdf5-dev
apt install -y libhdf5-serial-dev
apt install -y libatlas-base-dev
apt install -y libjasper-dev
apt install -y libqtgui4
apt install -y libqt4-test
apt install -y libraspberrypi-bin
apt install -y libatlas-base-dev

# Pip install
pip3 install vcgencmd
pip install rpi_ws281x
pip3 install rpi_ws281x --break-system-packages

# git init
git submodule init
git submodule update

# neo pixel lib
cd rpi_ws281x/python
python3 setup.py install
python3 ez_setup.py

cd -

#cd ~/ && git clone https://github.com/jgarff/rpi_ws281x
#cd rpi_ws281x
#mkdir build
#cd build
#cmake -D BUILD_SHARED=OFF -D BUILD_TEST=ON ..
#make install

echo "Installing"
chmod 777 *.py *.sh
ln -s $PWD/*.py /usr/local/bin
echo "Done"
