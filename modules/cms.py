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
    for keys, values in info.items():
        keys = keys.replace('-', ' ')
        keys = keys.title()
        print(Fore.BLUE + '\n' + keys + ' : ' + values)
    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()
