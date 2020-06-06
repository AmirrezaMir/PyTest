import sys
import requests
import ipapi
from colorama import Fore
import os

def start():
    os.system("clear")
    target = input(Fore.RED + 'enter a domain/ip --> ')
    ip = ipapi.location(ip=target, key=None, field=None)
    result = requests.get('https://api.hackertarget.com/dnslookup/?q='+ip['ip']).text
    print(Fore.BLUE + result)

    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()
