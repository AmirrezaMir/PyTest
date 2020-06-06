import sys
from colorama import Fore
import requests
import socket
import os

def start():
    os.system("clear")
    site = input(Fore.RED + 'Enter a website --> ')
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
    if site == '':
        try:
            sys.exit()
        except:
            return

    for sub in subdom:
        try:
            host = str(sub) + '.' + str(site)
            bypass = socket.gethostbyname(host)
            print(Fore.BLUE + 'Cloudflare bypass result for ' + Fore.CYAN + host + Fore.WHITE + ' | ' + Fore.BLUE + bypass )
        except Exception:
            pass

    try:
        input(Fore.GREEN + 'Back to Menu(press enter...) ')

    except:
        print('')
        sys.exit()

