from colorama import Fore
from requests import get
import os
import platform
from pystyle import Colors, Colorate




def updatetitle():
    if platform.system() == 'Windows':
        content = f"[Proxies Scraper] by R.F.E"
        os.system(f"title {content}")
def clear():
    if platform.system() != 'Windows':
        os.system('clear')
        return None
    os.system('cls')
def choices():
    clear()
    print(Colorate.Horizontal(Colors.blue_to_white,"""
     _____               _                _____                                
    |  __ \\             (_)              / ____|                               
    | |__) | __ _____  ___  ___  ___    | (___   ___ _ __ __ _ _ __   ___ _ __ 
    |  ___/ '__/ _ \\ \\/ / |/ _ \\/ __|    \\___ \\ / __| '__/ _` | '_ \\ / _ \\ '__|
    | |   | | | (_) >  <| |  __/\\__ \\    ____) | (__| | | (_| | |_) |  __/ |   
    |_|   |_|  \\___/_/\\_\\_|\\___||___/   |_____/ \\___|_|  \\__,_| .__/ \\___|_|   
                                                              | |              
                                Made By R.F.E                 |_|  """, 1))            


    from colorama import Fore, Back, Style

    
    print("  │ " +Fore.BLUE+"Proxies :"+Fore.RESET)
    print("  ├──────────")
    print("  │")
    print("  │ ["+Fore.BLUE+"1"+Fore.RESET+"] HTTP                ["+Fore.BLUE+"3"+Fore.RESET+"] socks 4")
    print("  │ ["+Fore.BLUE+"2"+Fore.RESET+"] HTTPS               ["+Fore.BLUE+"4"+Fore.RESET+"] socks 5")
    print("  │                                     ") 
 
    choice = input("  └───> ")

    if choice == "1": Proxies("-http")
    elif choice == "2": Proxies("-https")
    elif choice == "3": Proxies("-socks4")
    elif choice == "4": Proxies("-socks5")
    else: choices()

def Proxies(Type):
    r = get(f'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies{Type}.txt')
    data = r.text
    if Type == "":
    	file = f"Proxies-All.txt"
    else:
    	file = f"Proxies{Type}.txt"
    with open(file, "w+") as f:
        f.write(str(data))
    print(f"\t\t\t"+Fore.BLUE+"Proxies successfully update !"+Fore.RESET)
    input("\n\n\t\t\t Press enter to exit >")
    choices()
updatetitle()
choices()
