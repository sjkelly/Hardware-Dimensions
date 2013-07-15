#! /bin/bash
echo "Converting ODS to CSV..."
libreoffice --headless --convert-to csv --outdir ./csv ./ods/*.ods
echo "Starting CSV to JSON conversion script..."
./csv_to_json.py
echo "Finished!"

