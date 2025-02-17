import random

def check_attendance():
    """
    Function to check the attendance of an employee.
    It randomly determines whether the employee is present, absent, or working part-time.
    """
    attendance = random.choice([0, 1, 2])  # 0: Absent, 1: Full-time, 2: Part-time
    return attendance

def calculate_wage(emp_type):
    """
    Function to calculate the wage of an employee based on work type.
    Implements switch-case logic using dictionary mapping.
    """
    wage_per_hr = 20
    work_hours = {
        0: 0,   # Absent
        1: 8,   # Full-time
        2: 4    # Part-time
    }
    daily_wage = wage_per_hr * work_hours.get(emp_type, 0)
    return daily_wage

def calculate_monthly_wage():
    """
    Function to calculate the total wage for a month.
    Assumes 20 working days in a month.
    """
    total_wage = 0
    working_days = 20    
    for day in range(1, working_days + 1):
        emp_type = check_attendance()
        daily_wage = calculate_wage(emp_type)
        total_wage += daily_wage
        print(f"Day {day}: {daily_wage} Rs")    
    print(f"Total wage for the month: {total_wage} Rs")

if __name__ == "__main__":
    calculate_monthly_wage()





