# Olly Love
# Movie Rating Processor - FileHandler Class
# Reads in data and writes out processed data

import csv

class FileHandler:
    def __init__(self, filename, outputFileName):
        self.filename = filename
        self.outputFileName = outputFileName

    # Read in movie data to dictionary w movie as the key and list of ratings as the value
    # ie {'Mario': [A+, 1|4, 3|5], 'Wonka': [F, 3|5]...}
    # encoding to get rid of wierd garbage characters appearing in front of titles
    def get_csv_data(self):
        data = {}
        titleData = []
        titleLine = True
        try:
            with open(self.filename, 'r', encoding='utf-8-sig') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    for i in range(len(row)):
                        if titleLine:
                            titleData.append(row[i])
                            data[row[i]] = []
                        else:
                            if row[i] != '':
                                data[titleData[i]].append(row[i])
                    titleLine = False
        except Exception as e:
            print("An error reading the file occured.")                  
        
        return data

    # Takes list of dicts of movie data
    # appends to a csv file
    def dataOutput(self, processedData):
        try:
            with open(self.outputFileName, mode='a') as file:
                writer = csv.writer(file)
                for movieDict in processedData:
                    writer.writerow(movieDict.values())
        except Exception as e:
            print("An error writing the file occured.")
        print("Data has been written.")

