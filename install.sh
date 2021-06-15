#!/bin/bash
echo $PWD
cd $PWD
sudo apt install -y python3-dev python3-pip scons cmake swig
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
