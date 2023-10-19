#!/bin/bash


read file;
my_variable=""
while IFS= read -r line
    do
      if [ -z "$line" ]; then
        break
      else
            my_variable+="$line\n"
      fi
    done

while [ -e lockfile ]
    do
        echo "Serwer zajety"
        sleep 1
    done
echo -n > buforSerwera.txt;
echo $file > buforSerwera.txt
echo -e  $my_variable >> buforSerwera.txt
touch lockfile
echo "Wysłane do serwera"
