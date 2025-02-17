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
    switch_case = {
        0: "Employee is absent for the day so the daily wage is: 0",
        1: f"The Employee is present for full day so the daily wage is : {daily_wage}",
        2: f"The Employee is present for part-time so the wage is : {daily_wage}"
    }    
    print(switch_case.get(emp_type, "Invalid employee type"))

if __name__ == "__main__":
    emp_type = check_attendance()
    calculate_wage(emp_type)





