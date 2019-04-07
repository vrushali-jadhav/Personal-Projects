import random
import sys
from flask.app import Flask
from flask import jsonify, request, Response
import time
import os

#'Server' class represents the server
app = Flask(__name__)
class Server:
    def __int__(self):
        self.cpu = self.CPU()  

    #'CPU' class represents the CPU
    class CPU:
        def generateLog(self):
            return random.randint(0,100)  

@app.route("/log/<path:logPath>", methods=['PUT'])
def def_generateLog(logPath):
    if(request.method == 'PUT'):
        #form all the variables to be written to the file
        todaysDate = time.strftime("%Y%m%d")

        #a server object and 2 CPU objects representing 2 CPUs that it has
        server = Server()
        cpu1 = server.CPU()
        cpu2 = server.CPU()
        timeNow = time.strftime("%Y%m%d%H%M")

        #if the file doesn't exist, create a new file with todays date and write to it. Otherwise append to the file
        exists = os.path.isfile('/{0}/{1}.log'.format(logPath, todaysDate))
        if(not exists):
            fh = open('/{0}/{1}.log'.format(logPath, todaysDate),'w')
            fh.write('timestamp \t IP \t\t\t cpu_id \t usage\n')
            fh.write('{0} \t {1} \t 0 \t\t {2}\n'.format(timeNow, request.host,cpu1.generateLog()))
            fh.write('{0} \t {1} \t 1 \t\t {2}\n'.format(timeNow, request.host,cpu2.generateLog()))
        else:
            fh = open('/{0}/{1}.log'.format(logPath, todaysDate),'a')
            fh.write('{0} \t {1} \t 0 \t\t {2}\n'.format(timeNow, request.host,cpu1.generateLog()))
            fh.write('{0} \t {1} \t 1 \t\t {2}\n'.format(timeNow, request.host,cpu2.generateLog()))

        fh.close()
        return('Created') 

if __name__ == "__main__": 
    port = sys.argv[1]
    app.run(host = '127.0.0.1', port=port,debug=True)
    
       



    



    