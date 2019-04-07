import csv

csvAsList = []

def parseCSV(csvName):
    with open(csvName, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            csvAsList.append(row["ServersList"])    
            line_count += 1
        return csvAsList
