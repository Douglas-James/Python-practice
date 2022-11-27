class Employ():
  # create the class
  # this initialization method python is look for __init__
  def __init__(self, first_name, Last_name, salary) :
    self.fname = first_name
    self.lname = Last_name
    self.sal = salary
  
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

# create an instance of employ
new_employee = Employ("James", "Douglas", 1233300)
new_employee1 = Employ("Bob", "Squal", 32000)
new_employee2 = Employ("Squick", "Scream", 13)


# storing it inside of list
employees_list = [new_employee, new_employee1, new_employee2]

# Printing 
for employees in employees_list:  
  print(f"Full Name {employees.full_name()} : Salary ${employees.rise_salary()}")


    