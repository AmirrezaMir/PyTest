import socket
import sys
from datetime import datetime
from colorama import Fore

def start():
 
    # Clearing Terminal Window
    os.system("clear")
    
    # Asking for input 
    ip = input(Fore.RED + "Enter a IP/Domain to scan --> ")
    target = socket.gethostbyname(ip)
    
    # Scan start time
    t1 = datetime.now()
    
    # Scanning ports between 1 to 1024; Using some error handling
    try : 
        for port in range(1, 1025):
        	con = socket.socket(socket.AF_INET , socket.SOCK_STREAM)	# Connecting via IPV4 and TCP
        	con.settimeout(0.5)
        	result = con.connect_ex((target, port))
        	if result == 0 :
        		print(Fore.GREEN + "Port " + Fore.WHITE + str(port) + Fore.GREEN + " is open")
        	con.close()
    	
    except KeyboardInterrupt :
    	print("\nKeyboard Interruption ! !")
    	sys.exit()
    	
    except socket.gaierror :
    	print("\nCould not resolve host ! !")
    	sys.exit()
    	
    except socket.error :
    	print("\nCould Not connect to server ! !")
    	sys.exit()
    	
    # Scan finish time
    t2 = datetime.now()
    
    # Scan total time
    total = t2 - t1
    print("Scan Done In" + str(t2))
    
    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()

