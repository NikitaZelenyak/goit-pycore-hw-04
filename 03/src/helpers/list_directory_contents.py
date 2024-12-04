from pathlib import Path
from colorama import Fore

def list_directory_contents(p):
    path = Path(p)
    if not path.exists():
        print("Path is not exist")
    else:
        for el in path.rglob("*"):
            if el.is_dir():
              print(f"{Fore.BLUE} Dir: {el} {Fore.RESET}")
            elif el.is_file():
                print(f"{Fore.YELLOW} File: {el} {Fore.RESET}")
            else:
                print(f"{Fore.RED} {el} - is not file or dir {Fore.RESET}")

