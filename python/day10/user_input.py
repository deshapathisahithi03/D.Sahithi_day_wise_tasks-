import pandas as pd

# List to store multiple employees
employee_list = []

# Number of employees to input
n = int(input("Enter the number of employees: "))

for _ in range(n):
    emp_id = input("Enter emp_id: ")
    emp_name = input("Enter emp_name: ")
    emp_age = input("Enter emp_age: ")
    
    # Append as a dictionary
    employee_list.append({'emp_id': emp_id, 'emp_name': emp_name, 'emp_age': emp_age})

# Creating DataFrame
df = pd.DataFrame(employee_list)
df = pd.read_csv('data.csv')

#df.to_csv("data.csv",index=False)
#print("data frame is converted successfully to csv file")
