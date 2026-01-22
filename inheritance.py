# Problem 4.1: Vehicle Inheritance Hierarchy
# Scenario:
# Model a vehicle system using inheritance to represent different types of vehicles.
# Requirements:
# Create a base class Vehicle with attributes: brand , model , year
# Create a method start_engine() that prints "Engine started"
# Create a method display_info() that prints vehicle details
# Create a derived class Car that inherits from Vehicle and adds attribute num_doors
# Create a derived class Motorcycle that inherits from Vehicle and adds attribute has_sidecar
# Override display_info() in both derived classes to include their specific attributes
# Create a multilevel inheritance: Vehicle → Car → SportsCar (adds max_speed attribute)
# Create objects of each class and demonstrate inheritance




class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"Has Sidecar: {self.has_sidecar}")


class SportsCar(Car):
    def __init__(self, brand, model, year, num_doors, max_speed):
        super().__init__(brand, model, year, num_doors)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f"Max Speed: {self.max_speed} km/h")



v = Vehicle("Generic", "Model X", 2020)
v.start_engine()
v.display_info()

print("-----")

c = Car("Toyota", "Corolla", 2022, 4)
c.start_engine()
c.display_info()

print("-----")

m = Motorcycle("Honda", "CBR", 2021, False)
m.start_engine()
m.display_info()

print("-----")

s = SportsCar("Ferrari", "F8", 2023, 2, 340)
s.start_engine()
s.display_info()



# Scenario:
# Build an employee management system using inheritance to represent different employee types.
# Requirements:
# Create a base class Employee with attributes: name , employee_id , salary
# Create a method calculate_salary() that returns the salary
# Create a method display_info() that prints employee information
# Create a derived class Manager that inherits from Employee and adds attribute department
# Override calculate_salary() in Manager to return salary * 1.2 (20% bonus)
# Create a derived class Developer that inherits from Employee and adds attribute programming_language
# Override calculate_salary() in Developer to return salary * 1.1 (10% bonus)
# Create a multilevel inheritance: Employee → Manager → SeniorManager (adds team_size )
# Create objects of each class and demonstrate inheritance and method overriding



class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Base Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def calculate_salary(self):
        return self.salary * 1.2   # 20% bonus

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print(f"Total Salary: {self.calculate_salary()}")


class SeniorManager(Manager):
    def __init__(self, name, employee_id, salary, department, team_size):
        super().__init__(name, employee_id, salary, department)
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def calculate_salary(self):
        return self.salary * 1.1   # 10% bonus

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")
        print(f"Total Salary: {self.calculate_salary()}")


e = Employee("Ali", 101, 50000)
e.display_info()
print("Calculated Salary:", e.calculate_salary())

print("-----")

m = Manager("Sara", 102, 80000, "HR")
m.display_info()

print("-----")

sm = SeniorManager("Ahmed", 103, 100000, "Finance", 12)
sm.display_info()

print("-----")

d = Developer("Usman", 104, 70000, "Python")
d.display_info()
