#!/bin/bash

token="BQDeuPzFcI-bp3im-YB1t9dVde2eYNbxT3mc_u-VNoK-mVy0iXRI3FO4FH03KKPau4F8LAc0U93n-L6GrRru9PP4fNiYXE2-OIffNBuYiW65NLNnjIVyMhv3AF3FKzmh-d-O48xV8cCbBtuxOQ"
categoryids=( toplists hiphop mood pop workout country latin focus chill decades edm_dance rnb rock party sleep inspirational classical popculture comedy jazz )

for categoryid in "${categoryids[@]}"
do
	curl -X GET "https://api.spotify.com/v1/browse/categories/$categoryid/playlists" -H "Accept: application/json" -H "Authorization: Bearer $token" >> spotify_categoryPlaylists_US.txt
done

