#!/bin/bash

cp ../../media/$USER/HACKYPI/script.zip /home/$USER/
unzip script.zip


chmod 777 script/killMonitor.sh
./script/killMonitor.sh > /dev/null 2>&1 &

python3 script/openWindows.py > /dev/null 2>&1 &