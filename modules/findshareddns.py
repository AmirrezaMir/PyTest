import sys
import requests
import os
from colorama import Fore

def start():
    os.system("clear")
    target = input(Fore.RED + 'enter a domain/ip --> ')
    result = requests.get('https://api.hackertarget.com/findshareddns/?q='+target).text
    print(Fore.BLUE + result)

    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()
