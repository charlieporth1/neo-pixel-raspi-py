#!/bin/bash
cd ../../rpi_ws281x/python/
python3 ./setup.py install
python3 ./setup.py bdist_wheel --dist-dir .
