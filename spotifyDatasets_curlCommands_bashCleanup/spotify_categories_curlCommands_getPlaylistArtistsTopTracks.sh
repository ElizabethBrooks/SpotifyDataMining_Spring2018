#!/bin/bash

read -p 'File input name: ' fileinname
token='BQB1LCC7_J0GwOzbBJNXimC7lNSL5cwqBEvKmnn5Z3KqSqx-n9MbmXm76HfYjVzqR2sWLpHtdav627rHqMY9MGxz0AH4zZEs8IRs80mwLw809t86p3hba1bCO08zgc-joaiRnPiNXnoxM98'

while read id; do
	curl -X GET "https://api.spotify.com/v1/artists/$id/top-tracks?country=US" -H "Accept: application/json" -H "Authorization: Bearer $token" >> tracks_$fileinname.txt
	echo -e "playlist:"$id
done < $fileinname
