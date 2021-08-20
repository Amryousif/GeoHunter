from requests import get
from sys import argv, platform
from os import system

def clear():
    if platform == "linux":
        system("clear")
    elif platform == "win32":
        system("cls")

clear()

print(""" 
  ____            _   _             _            
 / ___| ___  ___ | | | |_   _ _ __ | |_ ___ _ __ 
| |  _ / _ \/ _ \| |_| | | | | '_ \| __/ _ \ '__|
| |_| |  __/ (_) |  _  | |_| | | | | ||  __/ |   
 \____|\___|\___/|_| |_|\__,_|_| |_|\__\___|_|   
    
    Coded by Muyrenit
    Github : Muyrenit
    Mail   : Muyrenit@gmail.com
                                              
""")

try:
    ip = argv[1]
    infoGet = get("http://ip-api.com/json/{}".format(ip))
    info = infoGet.json()
    print(""" 
        
       Country     : {}
       City         : {}
       Country Code  : {}
       Zip Code     : {}
       Isp         : {}       

        """.format(info['country'],info['city'],info['countryCode'],info['zip'],info['isp']))                      
            
except:
    clear()
    print("Usage : python3 GeoHunter.py <target_ip>") 
