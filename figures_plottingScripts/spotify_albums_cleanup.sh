#!/bin/bash

fileids=( aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az ba bb bc bd )
fileids1=( ap aq ar as at au av aw ax ay az ba bb bc bd )
fileids2=( aa ab ac ad ae af ag ah ai aj ak al am an ao )

for fileid in "${fileids[@]}"
do
	sed -n '/"uri" :/p' albums_"$fileid".txt > albums_"$fileid"_uri.txt
	sed 's/"uri" : "spotify:artist:.*//' albums_"$fileid"_uri.txt > albums_"$fileid"_uri_noDuplicates.txt
	sed 's/ //g' albums_"$fileid"_uri_noDuplicates.txt > albums_"$fileid"_uri.txt
	sed '/^\s*$/d' albums_"$fileid"_uri.txt > albums_"$fileid"_uri_noDuplicates.txt
	sed -r 's/.{21}//' albums_"$fileid"_uri_noDuplicates.txt > albums_"$fileid"_uri.txt
	sed -i 's|["]||g' albums_"$fileid"_uri.txt
	awk '!seen[$0]++' albums_"$fileid"_uri.txt > albums_"$fileid"_uri_noDuplicates.txt
	echo "$fileid done"
done

for ((i=0;i<${#fileids1[@]};++i)); do
	paste -d'\n' albums_"${fileids1[i]}"_uri_noDuplicates.txt albums_"${fileids2[i]}"_uri_noDuplicates.txt >> catagoriesAlbums_US_ids.txt
done
