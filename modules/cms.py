import requests
import builtwith
import sys
import os
from colorama import Fore

def start():
    os.system("clear")
    target = input(Fore.RED + 'enter a domain --> ')
    if not 'http://' in target and not 'https://' in target:
        target = 'http://' + target

    info = builtwith.parse(target)
    for i in info:
        value = ''
        for val in info[str(i)]:
            val = val.replace('-',' ')
            val = val.title()
            value += str(val)
        print(Fore.BLUE+"\n"+i+': '+value)

    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()
