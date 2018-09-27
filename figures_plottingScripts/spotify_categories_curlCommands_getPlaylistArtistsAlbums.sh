#!/bin/bash

read -p 'File input name: ' fileinname
token='BQC0R8ST2jvpTciVn-diQFmOtXBFegJGe7CdvQmlU3ywFg1YD5NTe0c60xWgiU2lJXlizBwpMRSJtq_DfoLgD2p4IGCPqCfq6b7eM6zJOvKO7p6Y60yfdqzOzDhpaDyd5B0RifGq1xb07x8'

while read id; do
	curl -X GET "https://api.spotify.com/v1/artists/$id/albums?market=US&limit=50" -H "Accept: application/json" -H "Authorization: Bearer $token" >> albums_$fileinname.txt
	echo -e "playlist:"$id
done < $fileinname
