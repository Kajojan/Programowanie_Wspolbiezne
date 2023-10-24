#!/bin/bash


read file;
# my_variable=""
# while IFS= read -r line
#     do
#       if [ -z "$line" ]; then # czy linijka jest pusta empty string 
#         break
#       else
#             my_variable+="$line\n"
#       fi
#     done
# #atomowosc
# while [ -e lockfile ] #czy plik  istnieje
#     do
#         echo "Serwer zajety"
#     done

# touch lockfile
# echo -n > buforSerwera.txt;
# echo $file > buforSerwera.txt
# echo -e  $my_variable >> buforSerwera.txt
# echo "Wysłane do serwera"
my_variable=""
while IFS= read -r line
do
    if [ -z "$line" ]; then
        break
    else
        my_variable+="$line\n"
    fi
done 

while ! { set -o noclobber; echo "$$" > ./lockfile;  } 2> /dev/null;
do
    echo "Serwer zajęty, proszę czekać"

done
set +o noclobber; 
echo "$file" > buforSerwera.txt
echo -e "$my_variable" >> buforSerwera.txt
echo "Wysłane do serwera"


    


