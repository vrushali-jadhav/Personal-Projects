import time
import datetime
import shlex
import FileAnalyser
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class CLU:
    def validate_ip(self, s):
        a = s.split('.')
        if len(a) != 4:
            return False
        for x in a:
            if not x.isdigit():
                return False
            i = int(x)
            if i < 0 or i > 255:
                return False
        return True

    def validate_port(self, port):
        if not (int(port)>= 0 and int(port)<=65535):
            return False
        else:
            return True

    def validate_date(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M')
            return True
        except:
            return False

    def menu(self, data_directory_path):
        print(bcolors.BOLD + "*** Welcome ***" + bcolors.ENDC)
        flag = True
        while(flag):
            print(bcolors.BOLD +"\nEnter the command to be executed (Or type '-h' for help and information on supported commands):\n"+bcolors.ENDC)
            chosenOption = input("")
            cmd = shlex.split(chosenOption)

            if(cmd[0] == "QUERY"):
                #validations
                
                #checking the format of the QUERY command is correct
                if(len(cmd)!= 5):
                    print(bcolors.FAIL+"Incorrect query format! Please refer help for correct format."+bcolors.ENDC)
                    continue
                
                ip = cmd[1].split(":")

                #validate IP
                if(not self.validate_ip(ip[0])):
                    print(bcolors.FAIL+"Invalid IP!"+bcolors.ENDC)
                    continue

                #validate port
                if(not self.validate_port(ip[1])):
                    print(bcolors.FAIL+"Invalid Port!"+bcolors.ENDC)
                    continue

                #validate CPU number
                if(int(cmd[2]) == 0 or int(cmd[2]) == 1):
                    pass
                else:
                    print(bcolors.FAIL+"Invalid CPU number!"+bcolors.ENDC)
                    continue

                #validate date format
                if(not (self.validate_date(cmd[3]) and self.validate_date(cmd[4]))):
                    print(bcolors.FAIL+"Incorrect date format. Please refer help for correct format."+bcolors.ENDC)
                    continue

                #validate that start date comes before end date
                if(datetime.datetime.strptime(cmd[3], '%Y-%m-%d %H:%M') > datetime.datetime.strptime(cmd[4], '%Y-%m-%d %H:%M')):
                    print(bcolors.FAIL+"Start date time has to be a datetime before end datetime."+bcolors.ENDC)
                    continue

                #analyse files
                file_ana = FileAnalyser.FileAnalyser(data_directory_path, cmd[1], cmd[2], cmd[3], cmd[4])
                results = file_ana.analiseFiles()
                print(results)

            elif(cmd[0] == "EXIT"):
                print(bcolors.WARNING + "Exiting..." + bcolors.ENDC)
                time.sleep(0.5)
                flag = False

            elif(cmd[0] == "-h"):
                print("The tool supports 2 commands:")
                print("\n'"+bcolors.BOLD+"QUERY"+bcolors.ENDC+"':")
                print("Takes a directory of data files as a parameter and lets you query CPU usage for a specific CPU in a given time period.")
                print("'QUERY' usage sample: QUERY 127.0.0.1:8080 0 '2019-03-30 10:57' '2019-04-01 11:01'")
                print("\n'"+bcolors.BOLD+"EXIT"+bcolors.ENDC+"':")        
                print("'EXIT' can be used anytime to exit the tool.")

            else:
                print(bcolors.WARNING+ "Invalid command" +bcolors.ENDC)

if __name__=="__main__":
    data_directory_path = sys.argv[1]
    clu = CLU()
    clu.menu(data_directory_path)
