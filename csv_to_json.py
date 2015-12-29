#! /usr/bin/env python3
import os
import csv
import json

print("Scanning CSV directory...")
csvFileList = os.listdir("./csv")

print("Generating JSON from CSV...")
for csvFile in csvFileList:
    with open("./csv/"+csvFile) as infile:
        reader = csv.DictReader(infile)
        name = os.path.basename(csvFile)
        name = os.path.splitext(name)[0]
        jsonFile = dict()
        jsonFile[name] = []
        for row in reader:
            for item in row: #turn number strings into floats
                try:
                    row[item] = float(row[item])
                except ValueError:
                    pass
            jsonFile[name].append(row)
        outFile = open("./json/"+name+".json", 'w')
        json.dump(jsonFile,outFile, indent=0, sort_keys=True)
        outFile.close()

print("CSV to JSON conversion finished!")
