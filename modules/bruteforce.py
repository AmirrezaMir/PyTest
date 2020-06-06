import requests
from colorama import Fore
import sys
import time

list = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']

def start():
    try:
        target = input(Fore.RED + 'enter a domain --> ')
        if 'http' in target:
            pass
        elif not 'http' in target:
            target = 'http://'+target
        
        for i in list:
            url = target + '/' + i
            time.sleep(0.3)
            r = requests.get(url)
            if r.status_code == 200 or r.status_code == 405:
                print(Fore.GREEN + '[+]' + url)
            else:
                print(Fore.RED + '[-]' + url)

        try:
            input(Fore.GREEN + 'Back to Menu(press enter...) ')

        except:
            print('')
            sys.exit()

    except:
        print('')
        sys.exit()
