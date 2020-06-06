import sys
import requests
import os
from colorama import Fore

def start():
    os.system("clear")
    url = input(Fore.RED + "Please enter a domain --> ")
    if 'http' not in url :
        url = 'http://' + url 
    r = requests.get(url)
    headers = r.headers
    
    for keys,values in headers.items() :
        print(Fore.BLUE + str(keys) + Fore.WHITE +  ':' + Fore.LIGHTCYAN_EX +  str(values))
        
    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()
