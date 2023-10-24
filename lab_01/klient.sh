#!/bin/bash

while true
do
        
        if [ -s wynik.txt ] #czy plik nie jest pusty 
        then
                cat wynik.txt;
                echo -n > wynik.txt;
        else
                read number;
                echo $number > dane.txt;
        fi;
        sleep 1
done