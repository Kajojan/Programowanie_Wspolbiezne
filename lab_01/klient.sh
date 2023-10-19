#!/bin/bash

while true
do
        read number;
        if [ -s wynik.txt ]
        then
                echo -n > wynik.txt;
                
                echo $number > dane.txt;
        else
                echo $number > dane.txt;
        fi;
done