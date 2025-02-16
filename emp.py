import random


def check_attendance():
    """
    Function to check the attendance of an employee.
    It randomly determines whether the employee is present or absent.
    """
    print("Welcome to Employee Wages Computation Program on Master Branch")   
    attendance = random.choice([1, 0])  # Randomly selects 1 (Present) or 0 (Absent)
    if attendance == 1:
        print("The employee is Present")
    else:
        print("The employee is Absent")

if __name__ == "__main__":
    """
    Main entry point of the program.
    Calls the check_attendance function and prints a welcome message.
    """
    check_attendance()
    print("Welcome To Employee Wage Computation")




