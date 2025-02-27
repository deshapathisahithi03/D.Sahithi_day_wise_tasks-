import csv

# Function to get employee details from user input
def get_employee_details():
    employee = []
    employee.append(input("Enter EmployeeID: "))
    employee.append(input("Enter Name: "))
    employee.append(input("Enter Position: "))
    employee.append(input("Enter Department: "))
    employee.append(input("Enter Email: "))
    employee.append(input("Enter Phone: "))
    return employee

# Define the CSV file path
csv_file_path = 'employee_details.csv'

# Open CSV file to append data
with open(csv_file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # If the file is empty, write headers
    file.seek(0, 2)  # Move cursor to end of file
    if file.tell() == 0:
        writer.writerow(["EmployeeID", "Name", "Position", "Department", "Email", "Phone", ])
    
    # Get details from user and write to file
    employee_details = get_employee_details()
    writer.writerow(employee_details)

print(f"Employee details have been added to '{csv_file_path}'.")
