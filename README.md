# **Menatic Sub Dominator**

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/Menatic007/Menatic-SubDominator?style=flat-square)
![GitHub](https://img.shields.io/github/repo-size/Menatic007/Menatic-SubDominator)
![GitHub](https://img.shields.io/github/forks/Menatic007/Menatic-SubDominator?style=flat-square)
![GitHub](https://img.shields.io/github/stars/Menatic007/Menatic-SubDominator?style=social)


![ezgif com-gif-maker](https://user-images.githubusercontent.com/102872534/186931473-696653d8-1bfd-41f9-9bac-fe3f66605078.gif)

* All **registered** subdomains!
* All **active** subdomains!
* All **Dns records**!
* Is **non-intrusive** - leave **NO fingerprints**, *totally fast and totally anonymous.*

## **Description** 

<p>Menatic Sub Dominator Gathers all registered subdomains for target domain, and then checks to see which ones are active subdomains, also will go through dns servers and do zonetransfer to see if any server have been mis-configured and are leaking valuable
information. Subdomains of a website are usually hidden and  are the main places where bug bounty hunters find their bugs from. This tool makes it easy to hunt down all these sub-domains and gather the following information if there is a vulnerability in the DNS server:<p>

* Owner/sys-admin email.
* Owner contact info.
* Server contact info.
* Ip addresses.
* Port numbers
* Telephone numbers.
* Location of server.
* Other servers
* Software.
* & more!.

Therfore this helps penetration testers and bug hunters collect and gather subdomains and information for the domain they are targeting. 

## Disclaimer !!!

<p>The exploits and malware built on this respository are mainly for POC and Educational purposes only. The developer is in no way responsible for any sort of misuse of tools and exploits or spreading of malware from this respository. If you use my tools in an illegal way, you will fully be responsible for your actions and not me.</p>


## Prerequisites

*From the standard libraries.*
* Time 
* Socket 
* Subprocess 
* os 
* Argparse 
* Json 

*Not from the standard libraries.*
* Colorama 
* Requests 
* Urlib3
## Installation

<code>

- git clone https://github.com/Menatic007/Menatic-SubDominator.git
  
- cd Menatic-SubDominator
  
- pip3 install -r requirements.txt

- Installation done, as simple as that.
  
</code> 

## Usage

<code>

To list all available options:

- python3 subdominator.py -h

- Example usage:

- python3 subdominator.py -d facebook.com -o facebook.txt

</code>

## Built With

* **Python 3.10.5** - [https://www.python.org/](https://www.python.org/)

## Key points

* Arguments are **-d** *(For domain)* & **-o** *(For output file)*
* Use http(s) in your domain.  ~  *Ex. -d https://example.com (Not https://www.example.com)*
* Specifying domain name is *NOT* optional.  ~  *Ex. -d https://example.com*
* Specifying output file *is* optional.  ~  *Ex. -o example.txt* 

**Note:**
- *100%*: You will get everything that can be possibly got from the domain/host all whilst leaving **NO** fingerprints. Enjoy










