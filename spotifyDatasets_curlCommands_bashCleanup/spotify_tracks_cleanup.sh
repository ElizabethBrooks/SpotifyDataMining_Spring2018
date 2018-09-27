#!/bin/bash

fileids=( aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az ba bb bc bd )
fileids1=( ap aq ar as at au av aw ax ay az ba bb bc bd )
fileids2=( aa ab ac ad ae af ag ah ai aj ak al am an ao )

for fileid in "${fileids[@]}"
do
	sed -n '/"uri" :/p' tracks_"$fileid".txt > tracks_"$fileid"_uri.txt
	sed 's/"uri" : "spotify:artist:.*//' tracks_"$fileid"_uri.txt > tracks_"$fileid"_uri_noDuplicates.txt
	sed 's/ //g' tracks_"$fileid"_uri_noDuplicates.txt > tracks_"$fileid"_uri.txt
	sed '/^\s*$/d' tracks_"$fileid"_uri.txt > tracks_"$fileid"_uri_noDuplicates.txt
	sed -r 's/.{21}//' tracks_"$fileid"_uri_noDuplicates.txt > tracks_"$fileid"_uri.txt
	sed -i 's|["]||g' tracks_"$fileid"_uri.txt
	awk '!seen[$0]++' tracks_"$fileid"_uri.txt > tracks_"$fileid"_uri_noDuplicates.txt
	echo "$fileid done"
done

for ((i=0;i<${#fileids1[@]};++i)); do
	paste -d'\n' tracks_"${fileids1[i]}"_uri_noDuplicates.txt tracks_"${fileids2[i]}"_uri_noDuplicates.txt >> catagoriesTracks_US_ids.txt
done
