#!/bin/bash

read -p 'File input name: ' fileinname
read -p 'File output name: ' fileoutname
read -p 'Bearer token: ' token

while read id; do
	curl -X GET "https://api.spotify.com/v1/artists/$id/related-artists" -H "Accept: application/json" -H "Authorization: Bearer $token" >> $fileoutname_$fileinname.txt
	echo -e "playlist:"$id
done < $fileinname.txt
