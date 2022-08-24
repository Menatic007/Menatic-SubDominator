# import modules

from re import A
import time
import urllib3
import subprocess
from subprocess import call
import os
import sys
import time
#from colorama import init, Fore, Back, Style
import requests
import json
import argparse
import socket
from argparse import RawTextHelpFormatter
color = True

machine = sys.platform # Detecting the os
if machine.lower().startswith(("os", "win", "darwin","ios")): 
    color = False # Colors will not be displayed on windows or Apple machines
if not color:
	reset = red = white = green  = blue = yellow = ""
else:                                                 
    white = "\033[97m"
    cyan = "\033[96m"
    red = "\033[91m"    
    reset = "\033[0m"
    green = "\033[92m"
    blue = "\033[34m"
    yellow = "\033[1;33m"


# Put ban banner here
print("Main Banner")

# Put sub banners here

print("Sub Banner")



def user_arguements():
    """
    This function takes arguements from the user through the terminal.
    """
    user_args = argparse.ArgumentParser(
    formatter_class=RawTextHelpFormatter,
    prog='Menatic Sub-Dominator',
    description=f'Menatic Subdominator v1.0 - created by Cyber Menatic | {green} https://github.com/Menatic007/Menatic-Buster {reset}',
    epilog=f'{white}Menatic Subdominator is a Sub-Domain finder that abuses certificate transparency to pull out sub-domains for a particular domain. Not just that, it also looks for for DNS information and vulnerabilities in the DNS server and perform a zone transfer if possible.{reset}')
    
    user_args.add_argument('-d', '--domain', type=str, required=True, help= "domain name, example: hackerone.com")
    user_args.add_argument('-o', '--output', type=str, required=False, help= 'Enter a name of a file in which you want to save your output in')
    passed_arguements = user_args.parse_args()
    
subdomains_alive = []
dns_servers = []

class Subdominator:
    def __init__(self):
        self.domain = user_arguements().domain
        self.output = user_arguements().output
        
    def url_parser(self):
        
        try:
            host = urllib3.utils.urlparse(self.domain).host
            
        except Exception as e:
            print("Check the domain you entered, it seems to be invalid my G")
            sys.exit()
        return host
    
    def request_json_data(self):
        subdomains = []
        try:
            request = request.get(f'https://crt.sh/?q=%.{Subdominator.url_parser()}&output=json')
            
            if request.status_code != 200:
                print(f'[-] host status-code: {request.status_code} using the certificate transparency method, try other domains or use different tools from Menatic007')
                
            else:
                try:
                    json_data = json.loads(request.text)
                    for subd in (json_data):
                        subdomains.append(subd['name_value'])
                except Exception as e:
                    print(f'json_data:Error{e}')
                    pass
        
        except Exception as e:
            print(f'request_json_data//Error: {e}')
            
        return subdomains
        

    def subdomains_alive(self):
        global alive_subdomains 
        for sub in Subdominator.request_json_data():
            try:
                sub = socket.gethostbyname(sub)
                if sub in alive_subdomains:
                    pass
                else:
                    alive_subdomains.append(sub)
            except:
                continue
            
        all_subdomains = len(Subdominator.request_json_data)
        numberofactive = len(alive_subdomains)
        
        try:
            print(f'\n\n{green}[+] There are{reset}{red}{str(all_subdomains)}REGISTERED{reset}{green}subdomains for this domain.{reset}') 
            
            time.sleep(2)
            
            index = f'{green}'+str('INDEX:green')
            sub_red = f'{reset}{red}'+str('SUBDOMAIN:red')
            line = f'{reset}{yellow}'+str('************************************')  
            
            print(f'\n{line}\n{index}\n{sub_red}\n{line}{reset}') 
            
            time.sleep(1.3)
            
            for index, sub in enumerate(Subdominator.request_json_data):
                print(f'{green}{str(index+1)}{reset} {red}{str(sub)}{reset}')
                
            print(f'\n\n{green}[+] There are{reset}{red}{str(numberofactive)}ACTIVE{reset}{green}subdomains for this domain.{reset}')
            time.sleep(2)  
            
            index = f'{green}'+str('INDEX:green')
            dns_white = f'{white}'+str('DNS SERVER:white')
            sub_red = f'{reset}{red}'+str('SUBDOMAIN:red')
            ip_add = f'{reset}{cyan} '+str('IP ADDRESS:cyan')
            line = f'{reset}{yellow}'+str('************************************')
            
            print(f'\n{line}\n{index}\n{dns_white}\n{sub_red}\n{ip_add}\n{line}{reset}')
            
            
            for index, sub in enumerate(alive_subdomains):
                print(f'{green} {str(index+1)}{reset} {white} {str(sub[0])}{reset} {red} {str(sub[1])} {reset} {cyan} {str(sub[2])}{reset}')
                
        except Exception as e:
            print(f'subdomains_alive//Error: {e}')
            pass
        
        return alive_subdomains
    
    
    def write_file(self):
        """
        This function writes the output to a file
        """      
        global alive_subdomains 
        try:
            if self.output is not None:
                reg = 'REGISTERED' + self.output
                active = 'ACTIVE' + self.output
                
                with open(reg, 'w') as r:
                    for index, sub in enumerate(Subdominator.request_json_data()):
                        text = f'{index} {sub} \n'
                        r.write(text)
                        
                with open(active, 'w') as a:
                    for index, sub in enumerate(Subdominator.request_json_data()):
                        text = f'{index} {sub} \n'
                        a.write(text)
                
                
        except Exception as e:
            print('write_file//Error: {e}')
            pass
        
        












