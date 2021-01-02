#!/bin/bash
echo "Installing"
echo $PWD
cd $PWD
sudo chmod 777 *.py *.sh
ln -s $PWD/*.py /usr/local/bin
echo "Done"
