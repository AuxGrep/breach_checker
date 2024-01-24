import argparse
import platform
import sys
import time
from configparser import ConfigParser
from colorama import Fore, Style
from prettytable import PrettyTable
from pyhibp import pwnedpasswords as hacker
import pyhibp
import urllib.request as con

# rangi
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL
cyan = Fore.CYAN
R = '\033[31m'  
G = '\033[32m'  
C = '\033[36m'  
W = '\033[0m'  
BOLD = "\033[1m"

Version = "1.0"

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

# Tuweke vikapu vyetu kwa ajili ya kuweka data 
email_breach = []
key_In = []

# Function au block ya kucheck kama single password ipo kwenye data breach
def pwned(passwd):
    try:
        pyhibp.set_user_agent(ua="Awesome application/0.0.1 (hacker is here)")
        resp = hacker.is_password_breached(password=str(passwd))
        print(f'{cyan}[Password_check: {passwd}] Checking if the password was breached{reset}')
        time.sleep(4)
        if resp:
            print(f"{red}Password breached!{reset}")
            print(f"This password was used {resp} time(s) before.")
            return resp
        else:
            print(f'{green}[Password_check]: {passwd} is SAFE to use{reset}')
    except KeyboardInterrupt:
        exit()

# Function ya kucheck kama PC ya user iko connected na Internet
def network(google='https://google.com'):
    try:
        con.urlopen(google)
        return True
    except:
        return False

# Function ya kucheck supported OS kama ni Windows, au Linux
def os_check(sup=['Linux', 'Windows']):
    try:
        if platform.system() not in sup:
            sys.exit(f'{red}Unsupported OS{reset}')
    except OSError as e:
        exit(f'An error occurred: {e}')

# Function ya kucheck kama email ipo kwenye databreach
def email_checker(key, email):
    try:
        pyhibp.set_user_agent(ua="Awesome application/0.0.1 (hacker is here)")
        pyhibp.set_api_key(key=str(key))
        resp2 = pyhibp.get_account_breaches(account=str(email), truncate_response=True)
        email_breach.append({'Email': email, 'Breaches': resp2})
        return resp2
    except TimeoutError:
        sys.exit('Connection timeout!! Try again later.')

# Main function
def main():
    parser = argparse.ArgumentParser(description='Check if a password or email has been breached OR NOT, Coded by AuxGrep.')
    parser.add_argument('--email', help='Check if an email has been breached')
    parser.add_argument('--password', help='Check if a password has been breached')
    args = parser.parse_args()

    if args.email:  # Check if --email argument is provided
        if network():  # Tuimeicall network connectivity Function ku-check kabla ya kuaanza kufanya
            os_check()
            key_In = []  # Move this inside the if statement for email checking
            config = ConfigParser()
            config.read('config.ini')
            if 'API' not in config:
                config['API'] = {}
            if 'key' not in config['API']:
                key_ = input('Enter API key (GET it from https://haveibeenpwned.com/API/Key): ')
                config['API']['key'] = key_
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
            key_In.append(config['API']['key'])
            for w in key_In:
                email_checker(key=str(w), email=args.email)
                if email_breach:
                    table = PrettyTable()
                    table.field_names = ['Email', 'Breaches']
                    for entry in email_breach:
                        table.add_row([entry['Email'], entry['Breaches']])
                    print(table)
        else:
            sys.exit(f'{red}Connect your PC to the Internet to access the network.{reset}')
    elif args.password:  # Check if --password argument is provided
        if network():  # Tuimeicall network connectivity Function ku-check kabla ya kuaanza kufanya
            os_check()
            breaches = pwned(passwd=args.password)
            if breaches:
                table = PrettyTable()
                table.field_names = ['Password', 'Breaches']
                table.add_row([args.password, breaches])
                print(table)
        else:
            sys.exit(f'{red}Connect your PC to the Internet to access the network.{reset}')
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
