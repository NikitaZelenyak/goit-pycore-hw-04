from data_helpers import read_data
from pathlib import Path
from get_cats_info import get_cats_info
current_dir = Path(__file__).parent

cuts_data = read_data(current_dir, "cuts_data.txt")
cuts_info = get_cats_info(cuts_data)
print(cuts_info)