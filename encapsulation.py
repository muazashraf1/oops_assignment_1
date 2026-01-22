# Problem 2.1: Student Grade Management
# Scenario:
# Create a Student class that manages student information and grades with proper encapsulation.
# Requirements:
# Use private attributes for: __name , __student_id , __grades (list)
# Create public methods: get_name() , get_student_id() , get_grades()
# Create a method add_grade(grade) that adds a grade to the private __grades list
# Create a method calculate_average() that returns the average of all grades
# Ensure that grades can only be added through the add_grade() method
# Create student objects and demonstrate that private attributes cannot be accessed directly


# ===== Solution

class Student:
    def __init__(self, name, student_id, grades):
        self.__name = name
        self.__student_id = student_id
        self.__grades = []
    
    def get_name(self):
        return self.__name
    def get_student_id(self):
        return self.__student_id
    def get_grades(self):
        return self.__grades
    
    def add_grade(self, marks):
        self.__grades.append(marks)
    
    def calculate_ave(self):
        # total =  sum(self.__grades)
        # count = len(self.__grades)
        # return total / count
        if len(self.__grades) == 0:
            return 0
        else:
            return sum(self.__grades) / len(self.__grades)

s1 = Student("Muaz", 20, 10)
s1.add_grade(20)
s1.add_grade(30)
s1.add_grade(40)

print(s1.calculate_ave())

# print(s1.__grade)   --> it is not possible 


# ===================================================================================

# Scenario:
# Build a Temperature class that stores temperature in Celsius and provides controlled access with validation.
# Requirements:
# Use a private attribute __celsius to store temperature
# Create a property celsius with getter and setter
# In the setter, validate that temperature is between -273.15 (absolute zero) and 1000
# Raise a ValueError if temperature is outside this range
# Create methods: to_fahrenheit() and to_kelvin() that return converted values
# Create temperature objects and demonstrate validation (try setting invalid temperatures)


# ===== Solution

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    @property
    def temp(self):
        return self.__celsius
    
    @temp.setter
    def temp(self, value):
        if value < -273.15 or value > 1000:
            raise ValueError("Temperature out of valid range")
        self.__celsius = value
    
    def to_fahrenheit(self):
        return (self.__celsius * (9/5)) + 32
    def to_kelvin(self):
        return self.__celsius + 273.15
    
t1 = Temperature(20)
print(t1.to_fahrenheit())
print(t1.to_kelvin())


try:
    t1.temp = -200
except ValueError as e:
    print(e)