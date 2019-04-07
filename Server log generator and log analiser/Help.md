1) What will you need?:

Python Flask and Python3.
ALl the commands are executed using python3.

2) Assumptions/freedom I took to design the program:
i) To similuate multi server environment, I have used differents ports. SO basically, the program has been tested with 5 servers. All of these 5 servers are running on localhost but on different ports.
ii) I have used a CSV that'll be passed to GenerateLog.py as input. This CSV file will have teh ip:port of the servers that are running and need to be monitored.

3) Use following commands to run the programs:
i) "python3 Server.py 8080" to start the server on localhost with port 8080
ii) "python3 GenerateLog.py /home/vrushali/LogGeneratorAnalyser/Logs /home/vrushali/LogGeneratorAnalyser/ServerList.csv", 1st arg is the path where the log files will be created
    2nd is the path where the csv file with server ips and port is present. 
    This file is responsibile for creating the log files and updating them every minute.
iii)"python3 CLU.py /home/vrushali/LogGeneratorAnalyser/Logs/" 
    This file is responsible for analysing the log files present on the specified path.
