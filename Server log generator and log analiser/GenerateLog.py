import Server
from flask.app import Flask
from flask import request, jsonify, json
import requests
import sys
import csv_paser 
import time

app = Flask(__name__)
class GenerateLogs:
    def __init__(self, logPath, server_list):
        while(True):
            for serverlink in server_list: 
                link = "http://{0}/log{1}".format(serverlink, logPath)
                with app.app_context():
                    r = requests.put(link)
                    print(r.text)
            time.sleep(60)

if __name__ == "__main__":
    logPath = sys.argv[1]
    csvPath = sys.argv[2]
    
    parsedCSVServerList = csv_paser.parseCSV(csvPath)
    generate = GenerateLogs(logPath,parsedCSVServerList)
