# PyPi is open source 3rd party for Python pkgs 
# like npm for node

# "pip install " to install pkgs
# pip install requests
# pip install colorama

from colorama import init
init() 
from colorama import Fore
print(Fore.RED + "some red text")
print(Fore.GREEN + "some GREEN text")
print(Fore.BLUE + "some BLUE text")