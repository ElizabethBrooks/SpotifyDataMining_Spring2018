#!/bin/bash

fileids1=( aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az ba bb bc bd )
fileids2=( bd bc bb ba az ay ax aw av au at as ar aq ap ao an am al ak aj ai ah ag af ae ad ac ab aa )

for ((i=0;i<${#fileids1[@]};++i)); do
	paste -d'\n' tracks_"${fileids2[i]}"_uri_noDuplicates.txt albums_"${fileids1[i]}"_uri_noDuplicates.txt >> catagoriesTotalTracks_US_ids.txt
	echo "${fileids2[i]} tracks merged with ${fileids1[i]} albums"
done

awk '!seen[$0]++' catagoriesTotalTracks_US_ids.txt  > catagoriesTotalTracks_US_ids_noDuplicates.txt
