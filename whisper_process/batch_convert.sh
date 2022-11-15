#!/bin/bash
INPUT=$1
OUTPUT=$2
#INPUT="/home/garret/dev/working/linux-unplugged/linux_unplugged_whisper_ingest.txt"
#OUTPUT="/home/garret/dev/whisper/linux-unplugged/"

LINES=$(cat $INPUT)
for AUDIOFILENAME in $LINES
do
    if [ -f "${AUDIOFILENAME##*/}.vtt" ]; then
	    echo "${AUDIOFILENAME##*/}.vtt exists. Passing..."
    else
	echo "${AUDIOFILENAME##*/}.vtt does not exist. Processing..."
	whisper ${AUDIOFILENAME} --output_dir $OUTPUT --model large --language English
    fi
done
