import sys
import requests
import os
from colorama import Fore
import json

def start():
    os.system("clear")
    site = input(Fore.RED + 'enter a domain --> ')
    target ={'remoteAddress':site}
    j = requests.post("https://domains.yougetsignal.com/domains.php", target)
    source =json.loads(j.content)

    for val in source['domainArray']:
        print(Fore.BLUE + val[0] + '\n')

    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()


