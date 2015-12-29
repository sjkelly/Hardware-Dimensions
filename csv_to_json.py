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
        for row in reader:
            partDict = dict()
            for item in row:
                if item == "size":
                    continue
                # turn number strings to floats if possible
                try:
                    partDict[item] = float(row[item])
                except ValueError:
                    partDict[item] = row[item]
            jsonFile[row["size"]] = partDict
        outFile = open("./json/"+name+".json", 'w')
        json.dump(jsonFile,outFile, indent=2, sort_keys=True)
        outFile.close()

print("CSV to JSON conversion finished!")
