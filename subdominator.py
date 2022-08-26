import time
import urllib3
import subprocess
from subprocess import call
import os
import sys
import time
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
    dark_cyan = "\033[32m"


# Put ban banner here
print(f"""{cyan}

• ▌ ▄ ·. ▄▄▄ . ▐ ▄  ▄▄▄· ▄▄▄▄▄▪   ▄▄·   .▄▄ · ▄• ▄▌▄▄▄▄· ·▄▄▄▄        • ▌ ▄ ·. ▪   ▐ ▄  ▄▄▄· ▄▄▄▄▄      ▄▄▄  
·██ ▐███▪▀▄.▀·•█▌▐█▐█ ▀█ •██  ██ ▐█ ▌▪  ▐█ ▀. █▪██▌▐█ ▀█▪██· ██  ▄█▀▄ ·██ ▐███▪██ •█▌▐█▐█ ▀█ •██   ▄█▀▄ ▀▄ █·
▐█ ▌▐▌▐█·▐▀▀▪▄▐█▐▐▌▄█▀▀█  ▐█.▪▐█·██ ▄▄  ▄▀▀▀█▄█▌▐█▌▐█▀▀█▄▐█▪ ▐█▌▐█▌.▐▌▐█ ▌▐▌▐█·▐█·▐█▐▐▌▄█▀▀█  ▐█.▪▐█▌.▐▌▐▀▀▄ 
██ ██▌▐█▌▐█▄▄▌██▐█▌▐█▪ ▐▌ ▐█▌·▐█▌▐███▌  ▐█▄▪▐█▐█▄█▌██▄▪▐███. ██ ▐█▌.▐▌██ ██▌▐█▌▐█▌██▐█▌▐█▪ ▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
▀▀  █▪▀▀▀ ▀▀▀ ▀▀ █▪ ▀  ▀  ▀▀▀ ▀▀▀·▀▀▀    ▀▀▀▀  ▀▀▀ ·▀▀▀▀ ▀▀▀▀▀•  ▀█▄▀▪▀▀  █▪▀▀▀▀▀▀▀▀ █▪ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀

{reset}""")

def user_arguements():
    """
    This function takes arguements from the user through the terminal.
    """
    user_args = argparse.ArgumentParser(
    formatter_class=RawTextHelpFormatter,
    prog='Menatic Sub-Dominator',
    description=f'Menatic Subdominator v1.0 - created by Cyber Menatic | {green} https://github.com/Menatic007/Menatic-Buster {reset}',
    epilog=f'{green}Menatic Subdominator is a Sub-Domain finder that abuses certificate transparency to pull out sub-domains for a particular domain. Not just that, it also looks for for DNS information and vulnerabilities in the DNS server and perform a zone transfer if possible.{reset}')
    
    user_args.add_argument('-d', '--domain', type=str, required=True, help= "domain name, example: hackerone.com", dest='domain', default=None)
    user_args.add_argument('-o', '--output', type=str, required=False, help= 'Enter a name of a file in which you want to save your output in', dest='output')
    passed_arguements = user_args.parse_args()
    return passed_arguements
    
subs_alive = []
dns_servers = []

class Subdominator:
    def __init__(self):
        self.domain = user_arguements().domain
        self.output = user_arguements().output
        
    def url_parser(self):
        
        try:
            host = urllib3.util.parse_url(self.domain).host
            
        except Exception as e:
            print(f"Invalid domain try again {e}")
            sys.exit(1)
        return host
    
    def request_json_data(self):
        subdomains = []
        
        try:
            r = requests.get(f'https://crt.sh/?q=%.{Subdominator.url_parser()}&output=json')
            
            if r.status_code != 200:
                print(f'[-] host status-code: {r.status_code} using the certificate transparency method, try other domains or use different tools from Menatic007')
                
            else:
                try:
                    json_data = json.loads(r.text)
                    for subd in (json_data):
                        subdomains.append(subd['name_value'])
                except Exception as e:
                    print(f'json_data:Error{e}')
                    pass
        
        except Exception as e:
            print(f'request_json_data//Error: {e}')
            
        return subdomains
        

    def subdomain_alive(self):
        global subs_alive 
        for sub in Subdominator.request_json_data():
            try:
                sub = socket.gethostbyname_ex(sub)
                if sub in subs_alive:
                    pass
                else:
                    subs_alive.append(sub)
            except:
                continue
            
        all_subdomains = len(Subdominator.request_json_data())
        numberofactive = len(subs_alive)
        
        try:
            print(f'\n\n{green}[+] THERE ARE{reset}{red} {all_subdomains} REGISTERED{reset}{green} SUBDOMAINS FOR THIS DOMAIN.{reset}\n') 
            
            time.sleep(2)
            print(f'{yellow}******************************************************************************************************{reset}')
            print(f'{green}INDEX : GREEN |{reset} {red}SUBDOMAIN : RED |{reset}')
            print(f'{yellow}******************************************************************************************************{reset}\n')
            
            
            time.sleep(1.3)
            
            for index, sub in enumerate(Subdominator.request_json_data()):
                print(f'{green}{index+1}{reset} {red}{sub}{reset}')
                
            print(f'\n\n{green}[+] THERE ARE{reset}{red} {numberofactive} ACTIVE{reset} {green} SUBDOMAINS FOR THIS DOMAIN.{reset}\n')
            
            time.sleep(2)  
            print(f'{yellow}******************************************************************************************************{reset}')
            print(f'{green}INDEX : GREEN |{reset} {white}DNS SERVER : WHITE |{reset} {red}SUBDOMAIN : RED |{reset} {cyan}IP ADDRESS : CYAN |{reset} {reset}\n{yellow}******************************************************************************************************{reset}\n\n')

            for index, sub in enumerate(subs_alive):
                ind = str(index +1)
                subz = str(sub[0])
                subo = str(sub[1])
                subt = str(sub[2])
                print(f'{green} {ind} |{reset}{white} {subz} |{reset} {red} {subo} |{reset} {cyan} {subt} |{reset}')
                
        except Exception as e:
            print(f'subdomains_alive// error {e}')
            pass
        
        return subs_alive
    
    
    def write_file(self):
        """
        This function writes the output to a file
        """      
        global subs_alive 
        try:
            if self.output is not None:
                reg = 'REGISTERED_' + self.output
                active = 'ACTIVE_' + self.output
                
                with open(reg, 'w') as r:
                    for index, sub in enumerate(Subdominator.request_json_data()):
                        text = f'{index} {sub} \n'
                        r.write(text)
                        
                with open(active, 'w') as a:
                    for index, sub in enumerate(subs_alive):
                        text = f'{index} {sub} \n'
                        a.write(text)
                
                
        except Exception as e:
            print(f'write_file//Error: {e}')
            pass
        

class DNS_ZONE_TRANSFER:
    def __init__(self):
        self.domain = Subdominator.url_parser()
        self.output = user_arguements().output
        
    def nslookup(self):
        line = f'{yellow}' + str(f'******************************************************************************************************{reset}')
        records = f'{red}' + str(f'[+] DNS{reset} {green}SERVERS AND RECORDS{reset}')
        print(f'{line}\n{records}\n{line}\n{green}')
        
        
        try:
            with open('dig.txt', 'w') as output_value:
                cmd = subprocess.call(f'dig -t ns {self.domain}', shell=True, stdout=output_value)
                print(subprocess.call(f'dig -t ns {self.domain}', shell=True))
            with open('dig.txt', 'r') as ns2:
                for line in ns2.readlines():
                    if '\tNS\t' in line:
                        line = line.split()[4]
                        dns_servers.append(line)
                        
        except Exception as e:
            pass
        return dns_servers
    
    def dns_records(self):
        print(f'{reset}{yellow}******************************************************************************************************{reset}')
        print(f'{red}[+] ATTEMPTING ZONE TRANSFER IF VULNERABILITY EXIST[+]{reset}')
        print(f'{yellow}******************************************************************************************************\n{reset}{green}')
        global dns_servers
        count = 0
        try:
            
            for ns in dns_servers:
                if self.output is not None:
                    filename = f'DNS_RECORDS_ {self.output}'
                    if count == 0:
                        with open(filename, 'w') as fp:
                            cmd = subprocess.call(f'dig axfr {Subdominator.url_parser()} @{ns}\n.\n', shell=True)
                            count +=1
                    
                    else:
                        with open(filename, 'a') as write_here:
                            cmd = subprocess.call(f'dig axfr {Subdominator.url_parser()} @{ns}\n.\n', shell=True)
                else:
                    cmd = subprocess.call(f'dig axfr {Subdominator.url_parser()} @{ns} \n.\n', shell=True)
                    
        except Exception as e:
            print(e)
            
        try:
            with open(filename, 'r') as rd:
                for line in rd.readlines():
                    print(line)
                    
        except:
            pass

if __name__ == '__main__':
    
    Subdominator = Subdominator()
    Subdominator.url_parser()
    Subdominator.request_json_data()
    Subdominator.subdomain_alive()
    Subdominator.write_file()
    
    #Perform Zone Transfer
    
    zone = DNS_ZONE_TRANSFER()
    zone.nslookup()
    zone.dns_records()
    
    print(f'{reset}{yellow}******************************************************************************************************{reset}')
    print(f"{red}CONGRATS MENATIC SUBDOMINATOR{reset} {green}HAS SUCCESSFULL FINISHED{reset}")
    print(f'{yellow}******************************************************************************************************{reset}')
    sys.exit(0)










