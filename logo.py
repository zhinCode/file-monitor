from colorama import Fore, Style, init

# 색상 초기화
init(autoreset=True)

# ASCII 로고
ASCII_LOGO = """
______  _  _       ___  ___              
|  ___|(_)| |      |  \/  |              
| |_    _ | |  ___ | .  . |  ___   _ __  
|  _|  | || | / _ \| |\/| | / _ \ | '_ \ 
| |    | || ||  __/| |  | || (_) || | | |
\_|    |_||_| \___|\_|  |_/ \___/ |_| |_|
                                         
"""

def display_logo():
    colors = [Fore.BLUE, Fore.MAGENTA]
    for i, line in enumerate(ASCII_LOGO.splitlines()):
        color = colors[i % len(colors)]
        print(f'{color}{line}{Style.RESET_ALL}')

def display_app_info(version, author, year):
    print(f'{Fore.CYAN}App Version: {version}{Style.RESET_ALL}')
    print(f'{Fore.CYAN}Author: {author}{Style.RESET_ALL}')
    print(f'{Fore.CYAN}Year: {year}{Style.RESET_ALL}')
