import json
import sys
import os
import requests
import time
from colorama import Fore

def start():
    os.system("clear")
    try:
        site = input(Fore.RED + 'enter a wordpress url without http --> ')
        s = requests.get('http://' + site + '/wp-content/plugins/')
        if s.status_code == 404 or s.status_code == 500:
            print(Fore.LIGHTRED_EX + 'Site is Not WordPress !!')
            time.sleep(1)
            sys.exit()
        else:
            pass
    except:
        time.sleep(0.5)
        sys.exit()

    try:
        url = 'http://' + site + '/wp-json/wp/v2/users/'
        r = requests.get(url).text
        j = json.loads(r)
        cn = 0
        user = ''
        for val in j:
            u = j[cn]['slug']
            if not u == '':
                user += Fore.GREEN + u + '\n'
            cn += 1
            if user == '':
                print(Fore.RED + 'Not Found ! !')

        print(user)
    except:
        time.sleep(0.5)
        sys.exit()

    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()
        
