
from colorama import Fore
import sys

from helpers.list_directory_contents import list_directory_contents

# path_example = Path(__file__).parent
print(sys.argv)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Будь ласка, надайте шлях до директорії як аргумент.")
    else:
        directory_path = sys.argv[1]
        print(f"{directory_path}")
        list_directory_contents(directory_path)