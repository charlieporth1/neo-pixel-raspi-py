#!/bin/bash

pyfiles=($(ls ../../*.py))
for file in $pyfiles
do
	sed -i 's|#!/usr/bin/env python3|#!/usr/bin/env python3.7|g' $file
done
