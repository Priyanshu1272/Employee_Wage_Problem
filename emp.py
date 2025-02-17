import random

def check_attendance():
    """
    Function to check the attendance of an employee.
    It randomly determines whether the employee is present or absent.
    """
    print("Welcome to Employee Wages Computation Program on Master Branch")
    attendance = random.choice([1, 0])  # Randomly selects 1 (Present) or 0 (Absent)
    return attendance

def emp_daily_wage():
    """
    Function to calculate the daily wage of an employee.
    Assumes wage per hour is 20 and full day is 8 hours.
    Also calculates part-time wage assuming part-time work is 4 hours.
    """
    wage_per_hr = 20
    full_day_hr = 8
    part_time_hr = 4  # Updated part-time hour assumption
    emp_check = check_attendance()
    if emp_check == 1:
        full_day_wage = wage_per_hr * full_day_hr
        part_time_wage = wage_per_hr * part_time_hr
        print(f"The Employee is present for full day so the daily wage is : {full_day_wage}")
        print(f"The Employee is present for part-time so the wage is : {part_time_wage}")
    else:
        print("Employee is absent for the day so the daily and part-time wage is: 0")

if __name__ == "__main__":
    emp_daily_wage()




