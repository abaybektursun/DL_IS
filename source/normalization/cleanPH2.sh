#!/bin/bash
find ../data/PH2Dataset/ -name "*_lesion" -print0 | while IFS= read -r -d $'\0' line; 
do
   rm -rf "$line"
done

find ../data/PH2Dataset/ -name "*_roi" -print0 | while IFS= read -r -d $'\0' line; 
do
   rm -rf "$line"
done

