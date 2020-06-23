import os
import socket
import sys
from datetime import datetime
from colorama import Fore 

def start():
    # Clear Terminal Windows
    os.system("clear")

    # Asking for Input, Then get the real ip address
    ip = socket.gethostbyname(input(Fore.RED + "Please Enter An IP Address To Scan\n >>> "))

    # Scan Start Time
    t1 = datetime.now()

    # Scanning Ports From 1 To 1024; Also Using some Error Handling
    try:
        for port in range(1, 1025):
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = connection.connect_ex((ip, port))
            if result == 0:
                print(Fore.GREEN + f"Port {port} is open")
            connection.close()

    except KeyboardInterrupt:
        print(Fore.RED + "Keyboard Interruption ! | Exiting ...")
        sys.exit()

    except socket.gaierror:
        print(Fore.RED + "Could Not Resolve The Host ! | Exiting ...")
        sys.exit

    except socket.error:
        print(Fore.RED + "Could Not Connect To server ! | Exiting ...")
        sys.exit()

    # Scan Finish Time
    t2 = datetime.now()

    # Estimated Time For Scan
    total = t2 - t1
    print(F"Scan Done in {total}")

    try : 
        input(Fore.GREEN + "Back To Menu...(Press Enter)")
        print("")
    except:
        sys.exit
