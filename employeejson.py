import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

def read_employees_from_json(file_path):
    employees = []
    with open(file_path, 'r') as file:
        data = json.load(file)
        for emp_data in data["employees"]:
            employee = Employee(
                emp_data["Name"],
                emp_data["DOB"],
                emp_data["Height"],
                emp_data["City"],
                emp_data["State"]
            )
            employees.append(employee)
    return employees

def print_employee_list(employees):
    for employee in employees:
        print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")

if __name__ == "__main__":
    employee_file_path = "employee.json"
    employee_list = read_employees_from_json(employee_file_path)
    print_employee_list(employee_list)
