import random

def check_attendance():
	"""
	Check employee attendance.
	This function randomly determines whether the employee is present (1) or absent (0).
	"""

	print("Welcome to Employee Wages Computation Program on Master Branch")
	attendance = random.choice([1, 0])
	return attendance

def emp_daily_wage():
	"""
	Calculate and display the employee daily wage.
	This function checks the employee attendance and calculates their daily wage 
	based on a fixed hourly rate. If the employee is present, the wage is calculated 
	for 8 hours; otherwise, the wage is 0.
	"""
	
	wage_per_hr = 20
	emp_check = check_attendance()
	if emp_check == 1:
		daily_wage = wage_per_hr * 8
		print(f"The Employee is present for full day so the daily wage is : {daily_wage}")
	else:
		daily_wage = 0
		print(f"Employee is absent for the day so the daily wage is: {daily_wage}")

if __name__=="__main__":
	emp_daily_wage()





