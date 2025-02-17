
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
    return daily_wage, work_hours.get(emp_type, 0)

def calculate_wage_with_conditions():
    """
    Function to calculate wages until a condition of total working hours (100)
    or total working days (20) is reached.
    """
    total_wage = 0
    total_hours = 0
    total_days = 0
    max_hours = 100
    max_days = 20
    
    while total_days < max_days and total_hours < max_hours:
        emp_type = check_attendance()
        daily_wage, hours_worked = calculate_wage(emp_type)      
        if total_hours + hours_worked > max_hours:
            break        
        total_wage += daily_wage
        total_hours += hours_worked
        total_days += 1
        print(f"Day {total_days}: {daily_wage} Rs, Hours Worked: {hours_worked}")    
    print(f"Total wage earned: {total_wage} Rs in {total_days} days and {total_hours} hours")

if __name__ == "__main__":
    calculate_wage_with_conditions()
