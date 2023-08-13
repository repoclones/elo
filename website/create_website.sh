#!/bin/bash

INPUT_FOLDER="src"
OUTPUT_FOLDER="neuroelo_web"

RUN_API_GENERATOR=true #the python scripts

# Loop through the arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        -n)
            RUN_API_GENERATOR=false
            shift
            ;;
        *)
            echo "Unknown argument: $1"
            exit 1
            ;;
    esac
done

cp $INPUT_FOLDER/* $OUTPUT_FOLDER/

tailwindcss -i $INPUT_FOLDER/styles.css -o $OUTPUT_FOLDER/styles.css -m

if [ "$RUN_API_GENERATOR" == true ]; then
	../venv/bin/python generate_api.py
fi
