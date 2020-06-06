import sys
import os
from colorama import Fore
import ipapi
import socket

def start():
    os.system("clear")
    try:
        target = input(Fore.RED + 'Enter a domain/ip --> ')
        source = ipapi.location(ip=target, key=None, field=None)

        print (Fore.BLUE+" ip = "+ source["ip"])
        print (Fore.BLUE+" city = " + source["city"])
        print (Fore.BLUE+" region = "+ source["region"])
        print (Fore.BLUE+" id country = "+source["country"])
        print (Fore.BLUE+" country = "+ source["country_name"])
        print (Fore.BLUE+" org = "+ source["org"])

        try:
            input(Fore.GREEN + 'Back to Menu(press enter...) ')

        except:
            print('')
            sys.exit()

    except:
        ip = socket.gethostbyname(target)
        source = ipapi.location(ip=ip, key=None, field=None)

        print (Fore.BLUE+" ip = "+ source["ip"])
        print (Fore.BLUE+" city = " + source["city"])
        print (Fore.BLUE+" region = "+ source["region"])
        print (Fore.BLUE+" id country = "+source["country"])
        print (Fore.BLUE+" country = "+ source["country_name"])
        print (Fore.BLUE+" org = "+ source["org"])

        try:
            input(Fore.GREEN + 'Back to Menu(press enter...) ')

        except:
            print('')
            sys.exit()        

