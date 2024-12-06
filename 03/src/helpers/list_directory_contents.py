from pathlib import Path
from colorama import Fore

def list_directory_contents(p):
    path = Path(p)
    if not path.exists():
        print("Path is not exist")
    else:
        for el in path.rglob("*"):
            pathList = str(el).split("/")
            if el.is_dir():
             
              print(f"{Fore.BLUE}{len(pathList) * "   "}{pathList[-1]}{Fore.RESET}")
            elif el.is_file():
                print(f"{Fore.YELLOW}{len(pathList) * "   "}{pathList[-1]} {Fore.RESET}")
            else:
                print(f"{Fore.RED} {pathList[-1]} - is not file or dir {Fore.RESET}")

