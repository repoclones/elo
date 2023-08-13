#!/bin/bash

INPUT_FOLDER=$"src"
OUTPUT_FOLDER=$"neuroelo_web"

cp $INPUT_FOLDER/* $OUTPUT_FOLDER/

#cp $INPUT_FOLDER/index.html $OUTPUT_FOLDER/
tailwindcss -i $INPUT_FOLDER/styles.css -o $OUTPUT_FOLDER/styles.css

#cp $INPUT_FOLDER/ $OUTPUT_FOLDER/
