#!/bin/bash

if [ -s wynik.txt ]
    then
        echo -n > wynik.txt;
        number="$1"
        echo $number > dane.txt;
else
        number="$1"
        echo $number > dane.txt;
fi;
