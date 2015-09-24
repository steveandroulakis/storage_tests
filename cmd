# all of this command (and the c) is fabulously bad! :D
while sleep 30; do FILENAME=$(date +'%Y-%m-%d-%H-%M-%S');START=$(date +%s.%N);./filewrite $FILENAME;END=$(date +%s.%N);NEWFILENAME=$(echo "t")$(echo "$END - $START" | bc)$(echo ".$FILENAME");mv $FILENAME $NEWFILENAME; done
