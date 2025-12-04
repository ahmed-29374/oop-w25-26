# my_age = 19
# my_name ="Sanjar"
# my_surname = "Baktybekov"
# print(f"Hello, my name is {my_name}, surname {my_surname}, a im {my_age}"  )

class Person:
    def __init__(self):
        self.name = "Sanjar"
        self.surname = "Baktybekov"
        self.age = 19


student = Person()

print(f"Hello, my name is {student.name}, surname {student.surname}, a im {student.age}"  )

class Animal:
    pass

dog = Animal()
dog.name = "Buddy"

print(f"My dog's name is {dog.name}")

#  The __init__() method is called automatically every time the class is being used to create a new object.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

my_car = Car("Porsche", "911", 2020)

print(f"My car is a {my_car.year} {my_car.brand} {my_car.model}")