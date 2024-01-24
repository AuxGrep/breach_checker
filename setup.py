import subprocess
import platform
import time
import os

Version = '1.0'

R = '\033[31m'  
G = '\033[32m'  
C = '\033[36m'  
W = '\033[0m'  
BOLD = "\033[1m"

required = ['prettytable', 'pyhibp', 'colorama', 'configparser']

def wozAA():
    banner = r'''
      ___                      _       ____                  _
    | ___ \                   | |     /  __ \ |             | |            
    | |_/ /_ __ ___  __ _  ___| |__   | /  \/ |__   ___  ___| | _____ _ __ 
    | ___ \ '__/ _ \/ _` |/ __| '_ \  | |   | '_ \ / _ \/ __| |/ / _ \ '__|
    | |_/ / | |  __/ (_| | (__| | | | | \__/\ | | |  __/ (__|   <  __/ |   
    \____/|_|  \___|\__,_|\___|_| |_|  \____/_| |_|\___|\___|_|\_\___|_| 

        '''
    
    print(G + banner + W)
    print(G + '[>]' + C + ' Coded by : ' + W + 'AuxGrep')
    print(G + '[>]' + C + ' Version    : ' + W + Version + '\n')
    print('')
wozAA()

def OS():
    try:
        if platform.system() == 'Windows':
            for setup in required:
                print(f'[--] Installing {setup}')
                subprocess.run(['pip', 'install', setup], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                time.sleep(3)

        elif platform.system() == 'Linux':
            for setup in required:
                print(f'[--] Installing {setup}')
                subprocess.run(['pip3', 'install', setup], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                time.sleep(3)
            
    except OSError as e:
        print(e)

OS()

