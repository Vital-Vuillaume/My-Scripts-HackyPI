#!/bin/bash

cp ../../media/$USER/HACKYPI/exemple2.sh /home/$USER/
cp ../../media/$USER/HACKYPI/app.py /home/$USER/


chmod 777 exemple2.sh


./exemple2.sh > /dev/null 2>&1 &
python3 app.py > /dev/null 2>&1 &