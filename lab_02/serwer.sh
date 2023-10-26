#!/bin/bash
while true
do
  if [ -e lockfile ]  #czy plik istnieje i buforSerwer nie jest pusty
  then
    licznik=0
    file=""
   cat buforSerwera.txt | while IFS= read -r line 
        do 
            if [ $licznik -eq 0 ]
            then
                file=$line
                echo $file
                touch $file
            else
                echo $line >> $file

            fi
            ((licznik++));

        done 
        sleep 5
        rm  lockfile

  fi;
done;