import sys
import requests
import os
import ipapi
from colorama import Fore

def start():
    os.system("clear")
    target = input(Fore.RED + 'Enter a website/domain --> ')
    ip = ipapi.location(ip=target, key=None, field=None)
    result = requests.get('http://api.hackertarget.com/whois/?q='+ ip['ip']).text
    print(Fore.BLUE + result)

    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()

