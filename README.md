# Menatic Sub Dominator



* All **registered** subdomains!
* All **active** subdomains!
* All **Dns records**!
* Is **non-intrusive** - leave **NO fingerprints**, *totally fast and totally anonymous.*

<img src = [![unknown.png](https://i.postimg.cc/DZLWD4Vc/unknown.png)](https://postimg.cc/r0yFRmwd)> </img>


**Menatic Sub-Dominator** - <p>Gathers all registered subdomains for target domain, and then checks too see which ones are active subdomains, also will go through dns servers and do zonetransfer to see if any server have been miss configured and are leaking valuable
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

## Installation

<code>

- git clone https://github.com/Menatic007/Menatic-SubDominator.git
  
- cd Menatic-SubDominator
  
- pip3 install -r requirements.txt

- Installation done as simple as that
  
</code> 

## Usage

<code>

To list all available options:

- python3 subdominator.py -h

- Example usage:

- python3 subdominator.py -d facebook.com -o facebook.txt

</code>


**Key points**
* Arguments are **-d** *(For domain)* & **-o** *(For output file)*
* Use http(s) in your domain.  ~  *Ex. -d https://example.com (Not https://www.example.com)*
* Specifying domain name is *NOT* optional.  ~  *Ex. -d https://example.com*
* Specifying output file *is* optional.  ~  *Ex. -o example.txt* 

**Note:**
- *100%*: You will get everything that can be possibly got from the domain/host all whilst leaving **NO** fingerprints.

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

## Usage example:




## Built With

* **Python 3.10.5** - [https://www.python.org/](https://www.python.org/)









