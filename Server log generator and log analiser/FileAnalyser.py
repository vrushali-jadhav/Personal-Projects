import os
from datetime import timedelta, date, datetime
import re

class FileAnalyser:
    def __init__(self, path, ipport, cpu, start_datetime, stop_datetime):
        self.dir_path = path
        self.ipport = ipport
        self.cpu = int(cpu)
        self.start_datetime = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M')
        self.start_date = datetime.date(self.start_datetime)
        self.stop_datetime = datetime.strptime(stop_datetime, '%Y-%m-%d %H:%M')
        self.stop_date = datetime.date(self.stop_datetime)

        self.analiseFiles()        


    def daterange(self, start_date, end_date):
        for n in range(int ((end_date - start_date).days)+1):
            yield start_date + timedelta(n)

    def analiseFiles(self):
        results = []
        list_of_files_to_scan = []

        for single_date in self.daterange(self.start_date, self.stop_date):
            stringDate = re.sub('[-]', '', str(single_date))

            list_of_files_to_scan.append("{0}.log".format(stringDate))
        
        for file in list_of_files_to_scan:
            try:
                with open("{0}/{1}".format(self.dir_path,file), 'r') as f:
                    for line in f:
                        line = re.sub('[\n]', '', line)
                        line = re.sub('[\t]', '', line)
                        splitLine = line.split(" ")
                        
                        if(splitLine[2]==self.ipport and int(splitLine[4])==self.cpu):
                            dateinstring = splitLine[0]
                            date = datetime(int(dateinstring[:4]),int(dateinstring[4:6]), int(dateinstring[6:8]),int(dateinstring[8:10]),int(dateinstring[10:12]))
                            
                            if date >= self.start_datetime and date <= self.stop_datetime:
                                entry = "({0}, {1}%)".format(date,splitLine[6])
                                results.append(entry)
                            
            except FileNotFoundError:
                pass

        return results


