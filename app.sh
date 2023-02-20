#!/bin/bash
rm result.txt

start_text="\begin{Verbatim}[numbers=left, frame=single]"
end_text="\end{Verbatim}"
current_file=""

for files in $(find . | egrep '.html|.py|.css')
# for files in $(find . -name "*.{html, py}")
do
    # echo "${files}"
    echo "  " >> result.txt
    echo "  " >> result.txt
    echo "\subsubsection{${files}}" >> result.txt
    echo "${start_text}" >> result.txt
    while read line
    do
        echo "$line" >> result.txt
    done < ${files}
    echo "${end_text}" >> result.txt

    # for line in $(cat ${files})
    # do
    #     echo "${line}"
    # done
done
current_folder="Welcome/to/LinuxHint"
#Define the string alue
text="Welcome/to/LinuxHint"

# Set space as the delimiter
IFS='/'

echo ${#current_folder}
echo "${current_folder}[2]"