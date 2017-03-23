#!/bin/bash
mkdir ../data/normalized
img_counter=0
find ../data/PH2Dataset/ -type f -iname "*.bmp" -print0 | while IFS= read -r -d $'\0' line; 
do
    ./Normalization "$line" ../data/normalized/${img_counter}.jpg
    let img_counter=img_counter+1
done