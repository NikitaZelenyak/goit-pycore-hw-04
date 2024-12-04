def salary_calculate(data):
    salaries = 0
    for employee in data:
        _, salary = employee.split(",")
        salaries += int(salary)
    return salaries, salaries / len(data)