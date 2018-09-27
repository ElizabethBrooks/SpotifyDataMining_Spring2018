#!/bin/bash

read -p 'File input name ending: ' fileinname
read -p 'Bearer token: ' token

while read id; do
	curl -X GET "https://api.spotify.com/v1/artists/$id/albums?market=US&limit=50" -H "Accept: application/json" -H "Authorization: Bearer $token" >> albums_$fileinname.txt
	echo -e "playlist:"$id
done < spotify_artistIds_US_noDuplicates_$fileinname
