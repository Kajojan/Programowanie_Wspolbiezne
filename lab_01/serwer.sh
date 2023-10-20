#!/bin/bash


while true
do
  if [ -s dane.txt ] #czy plik nie jest pusty 
  then
    read -r number < dane.txt;
    echo $((number + 3)) > wynik.txt;
    echo -n > dane.txt;
  fi;
done;