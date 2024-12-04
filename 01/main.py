from pathlib import Path
from data_helpers import read_data
from salary_calculate import salary_calculate
current_dir = Path(__file__).parent

data_employees = read_data(current_dir, "db.txt")

total, average = salary_calculate(data_employees)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

 




