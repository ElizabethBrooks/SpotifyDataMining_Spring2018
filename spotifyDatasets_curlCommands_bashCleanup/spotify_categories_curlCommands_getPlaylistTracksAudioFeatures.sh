#!/bin/bash

read -p 'File input name: ' fileinname
token='BQCYh155p4jljOCIUss8mH0XAbLxuP60QhdsDYWe5_Z45hk4F6t4CDWrXH37ObAZNYNOyhb_5cE5DmzYeipNNJ_cldbt73xSWCqOLIv5h8QIeIRcZHSTy2sfxF3frZipP0x0FT5BVnA2DH2ZiA'

while mapfile -t -n 100 ary && ((${#ary[@]})); do
	echo -e "${ary[@]}" >> catagoriesTracksFeatures_$fileinname.txt
done < catagoriesTotalTracks_US_ids_noDuplicates_$fileinname.txt

sed 's/ /,/g' catagoriesTracksFeatures_$fileinname.txt > catagoriesTracksFeatures_inputs_$fileinname.txt

while read id; do
	curl -X "GET" "https://api.spotify.com/v1/audio-features?ids=$id" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer $token" >> trackFeatures_$fileinname.txt
done < catagoriesTracksFeatures_inputs_$fileinname.txt
