#!/bin/bash

fileids=( a b c d e f g h )
fileids1=( d c b a )
fileids2=( e f g h )

while IFS=, read trackid popularity;do
	sed -i "/^$trackid/ s/$/,$popularity/" trackFeatures_"${fileids[i]}"_totalTrackFeatures.txt
done < trackData_"${fileids[i]}"_totalTrackData.txt

for ((i=0;i<${#fileids2[@]};++i)); do
	paste -d'\n' trackFeatures_"${fileids2[i]}"_totalTrackFeatures.txt trackFeatures_"${fileids1[i]}"_totalTrackFeatures.txt >> trackFeatures_totalTrackFeatures2.txt
	echo -e "${fileids2[i]} merged with ${fileids1[i]}"
done

sed '/^\s*$/d' trackFeatures_totalTrackFeatures2.txt > trackFeatures_totalTrackFeatures.txt

wc -l trackFeatures_totalTrackFeatures2.txt
wc -l trackFeatures_totalTrackFeatures.txt
