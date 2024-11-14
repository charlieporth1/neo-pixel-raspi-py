#!/bin/bash
python3 ../../rpi_ws281x/python/setup.py install
python ../../rpi_ws281x/python/setup.py bdist_wheel --dist-dir .
