import ctypes.wintypes, ctypes, requests, os, sys
from colorama import init, Fore, Style
from pystyle import Center

init()

count = 0
liste = ['1', '2', 'cls']
ctypes.windll.kernel32.SetConsoleTitleW('Hypesquad Changer 2024')

os.system("cls")

banner1 = '''
██╗  ██╗██╗   ██╗██████╗ ███████╗███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ 
██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔══██╗
███████║ ╚████╔╝ ██████╔╝█████╗  ███████╗██║   ██║██║   ██║███████║██║  ██║
██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ╚════██║██║▄▄ ██║██║   ██║██╔══██║██║  ██║
██║  ██║   ██║   ██║     ███████╗███████║╚██████╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝                                                                         
'''

def Start():
    print(Center.XCenter(banner1))
    print(Center.XCenter(f"{Fore.WHITE}╔═════════════════════════╗╔═════════════════════════╗"))
    print(Center.XCenter(f"{Fore.WHITE}                             ║[{Fore.BLUE}1{Fore.WHITE}] - {Fore.BLUE}House Changer   {Fore.WHITE}   ║║ # {Fore.BLUE}Sowqa Hypesquad     {Fore.WHITE}  ║"))
    print(Center.XCenter(f"{Fore.WHITE}                             ║[{Fore.BLUE}2{Fore.WHITE}] - {Fore.BLUE}Exit            {Fore.WHITE}   ║║ # {Fore.BLUE}Github: @sowqa      {Fore.WHITE}  ║"))
    print(Center.XCenter(f"{Fore.WHITE}╚═════════════════════════╝╚═════════════════════════╝"))

def hypesquad_changer():
    token = input(f"{Fore.BLUE}Enter your discord token {Fore.WHITE}> {Fore.BLUE}")
    url = 'https://discord.com/api/v10/hypesquad/online'
    
    def rate_limited():
        print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED} An error has occurred, your token is rate limited.\n')

    def invalid_token():
        print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED} An error has occurred, your token is invalid.\n')

    while True:
        option = input(f'{Fore.WHITE}[{Fore.BLUE}1{Fore.WHITE}] {Fore.BLUE}Hypersquad Bravery (Purple)\n{Fore.WHITE}[{Fore.BLUE}2{Fore.WHITE}] {Fore.BLUE}Hypersquad Brilliance (Red)\n{Fore.WHITE}[{Fore.BLUE}3{Fore.WHITE}] {Fore.BLUE}Hypersquad Balance (Green)\n\n{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.BLUE} Select a Discord Badge {Fore.WHITE}> {Fore.BLUE}')
        
        if option in ['1', 'Hypersquad Bravery', 'House of Bravery', 'Bravery']:
            house_of_bravery = requests.post(url, json={'house_id': '1'}, headers={'authorization': token})
            if house_of_bravery.status_code == 204:
                print(f'{Fore.WHITE}[{Fore.GREEN}Welcome{Fore.WHITE}] {Fore.GREEN} You\'ve joined the Hypesquad Bravery.\n')
            elif house_of_bravery.status_code == 429:
                rate_limited()
            elif house_of_bravery.status_code == 401:
                invalid_token()
                break
            else:
                print(f'{house_of_bravery.text}\n')
        
        elif option in ['2', 'Hypersquad Brilliance', 'House of Brilliance', 'Brilliance']:
            house_of_brilliance = requests.post(url, json={'house_id': '2'}, headers={'authorization': token})
            if house_of_brilliance.status_code == 204:
                print(f'{Fore.WHITE}[{Fore.GREEN}Welcome{Fore.WHITE}] {Fore.GREEN} You\'ve joined the Hypesquad Brilliance.\n')
            elif house_of_brilliance.status_code == 429:
                rate_limited()
            elif house_of_brilliance.status_code == 401:
                invalid_token()
                break
            else:
                print(f'{house_of_brilliance.text}\n')
        
        elif option in ['3', 'Hypersquad Balance', 'House of Balance', 'Balance']:
            house_of_balance = requests.post(url, json={'house_id': '3'}, headers={'authorization': token})
            if house_of_balance.status_code == 204:
                print(f'{Fore.WHITE}[{Fore.GREEN}Welcome{Fore.WHITE}] {Fore.GREEN} You\'ve joined the Hypesquad Balance.\n')
            elif house_of_balance.status_code == 429:
                rate_limited()
            elif house_of_balance.status_code == 401:
                invalid_token()
                break
            else:
                print(f'{house_of_balance.text}\n')

        else:
            print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED} An error has occurred, you have chosen the wrong option.\n')

def commands():
    option = input(f"\n{Fore.BLUE}Choice {Fore.WHITE}> {Fore.BLUE}")
    if option not in liste:
        print(f'\n{Fore.RED}Invalid Selection')
        commands()
    elif option == '1':
        hypesquad_changer()
    elif option == '2':
        input(f'\n{Fore.BLACK}{Style.BRIGHT}Press enter to exit{Style.RESET_ALL}')
        sys.exit(0)
    elif option == 'cls':
        os.system('cls')
        Start()
        commands()

Start()
while True:
    try:
        commands()
    except KeyboardInterrupt:
        print('')
        pass
