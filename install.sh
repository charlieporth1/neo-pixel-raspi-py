#!/bin/bash
echo $PWD
cd $PWD
sudo apt install -y python3-dev python3-pip scons cmake swig git
sudo apt-get install -y build-essential python-dev git scons swig libzbar-dev libzbar0
sudo apt install -y python python-pip libffi-dev python-backports.ssl-match-hostname
sudo apt-get install libcblas-dev
sudo apt-get install libhdf5-dev
sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test
sudo apt install libraspberrypi-bin
sudo apt-get install libatlas-base-dev

sudo pip3 install vcgencmd
sudo pip3 install rpi_ws281x
sudo pip install rpi_ws281x
git submodule init
git submodule update
cd rpi_ws281x/python
sudo python3 setup.py  install
cd -
#cd ~/ && git clone https://github.com/jgarff/rpi_ws281x
#cd rpi_ws281x
#mkdir build
#cd build
#cmake -D BUILD_SHARED=OFF -D BUILD_TEST=ON ..
#sudo make install

echo "Installing"
sudo chmod 777 *.py *.sh
ln -s $PWD/*.py /usr/local/bin
echo "Done"
