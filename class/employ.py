class Department(): 
  def __init__(self, name):
      self.name = name
      self.employees = []
  
  # adding employee
  def add_employee(self, employee):
    if employee not in self.employees:
      self.employees.append(employee)

  # print_employee info
  def print_employee_info(self) :
    if not self.employees:
      print(f"No employeees in {self.name}")
    for employee in self.employees:
      print(f"{employee.fname[0]}. {employee.lname[0:3]} - Salary: {employee.sal}")

  # _str_
  def __str__(self):
      if len(self.employees) <= 1:
          return f"{self.name} ({len(self.employees)}) employee"
      else:
          return f"{self.name} ({len(self.employees)}) employees"


class Employ():
  # create the class
  # this initialization method python is look for __init__
  def __init__(self, first_name, Last_name, salary, department) :
    self.fname = first_name
    self.lname = Last_name
    self.sal = salary
    self.department = department
    self.department.add_employee(self)
  
  # method full name that return full name 
  def full_name(self):
      return  f"{self.fname} {self.lname}"
  
  def rise_salary(self):
      if(self.sal > 20000000):
        return  f" Can't make it more than This salary ${self.sal}"
      elif (self.sal < 400000):
          return  self.sal * 1.5
      else:
          return f"something went wrong salary: ${self.sal}"



# create an instance Department
department_1 = Department("Sale")
department_2 = Department("Engineering")
department_3 = Department("HR")
department_4 = Department("Legal")

departments = [department_1, department_2, department_3, department_4]

# create an instance of employ
new_employee = Employ("James", "Douglas", 1233300, department_2)
new_employee1 = Employ("Bob", "Squal", 32000, department_1)
new_employee2 = Employ("Squick", "Scream", 13, department_3)
new_employee = Employ("R", "Douglas", 81000, department_1)


# storing it inside of list
employees_list = [new_employee, new_employee1, new_employee2]

# Printing  employee
# for employees in employees_list:  
#   print(f"Full Name {employees.full_name()} : Salary ${employees.rise_salary()}")


# Printing Department
for dep in departments:
    print(dep)
    dep.print_employee_info()