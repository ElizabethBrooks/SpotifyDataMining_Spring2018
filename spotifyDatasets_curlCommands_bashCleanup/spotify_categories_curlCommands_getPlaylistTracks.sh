#!/bin/bash

read -p 'File input name: ' fileinname
token='BQBK6wmrk2qT6JwAncJUum20XP5SDLcJK0sJk6fZlS2lWRE-bxETfYHkZraIZ0nv5-A3EP8p7rQfSZCzt52IsLzwjANLbmHGg6saXS0ElKn6nPOLt_yqIH0EUAfrtapz5qzVKedZ_001osvQEg'

while mapfile -t -n 50 ary && ((${#ary[@]})); do
	echo -e "${ary[@]}" >> catagoriesTotalTracksData_$fileinname.txt
done < catagoriesTotalTracks_US_ids_noDuplicates_$fileinname.txt

sed 's/ /,/g' catagoriesTotalTracksData_$fileinname.txt > catagoriesTotalTracksData_inputs_$fileinname.txt

while read id; do
	curl -X "GET" "https://api.spotify.com/v1/tracks?ids=$id&market=US" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer $token" >> trackData_$fileinname.txt
done < catagoriesTotalTracksData_inputs_$fileinname.txt
