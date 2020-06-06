import sys
import requests
import os
import ipapi
from colorama import Fore

def start():
    os.system("clear")
    target = input(Fore.RED + 'enter ip/domain --> ')
    ip = ipapi.location(ip=target, key=None, field=None)
    result = requests.get('https://api.hackertarget.com/mtr/?q='+ip['ip']).text
    print(Fore.BLUE + result)

    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()

