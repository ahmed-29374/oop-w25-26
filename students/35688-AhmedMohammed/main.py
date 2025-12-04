#python oop practice from w3schools

#class
class Car:
    brand = "Toyota"   # class variable i think

c = Car()
print(c.brand)


#__init__ method
class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

p1 = Person("ahmed", 20)
print(p1.name)


#self parameter 
class Dog:
    def __init__(self, name):
        self.name = name   #using self saves value inside object

    def bark(self):
        print(self.name, "woof")

d1 = Dog("loki")
d1.bark()


#class property
class Student:
    school = "warsaw university"   # property shared by all students

    def __init__(self, name):
        self.name = name

s1 = Student("maria")
print(s1.school)


#class method
class MathThings:
    @classmethod
    def add2(cls, x):
        return x + 2

print(MathThings.add2(9))


#inheritance
class Animal:
    def sound(self):
        print("animal sound")

class Cat(Animal):   #cat gets animal stuff
    pass

c1 = Cat()
c1.sound()


# polymorphism (same func name but diff output)
class Bird:
    def sound(self):
        print("tweet")

class Cow:
    def sound(self):
        print("moo")

for a in (Bird(), Cow()):
    a.sound()


#encapsulation idea
class Bank:
    def __init__(self):
        self._balance = 100   

    def get_balance(self):
        return self._balance

b = Bank()
print(b.get_balance())


#iinner class
class Company:
    def __init__(self, name):
        self.name = name
        self.dep = self.Department()  #the inner object

    class Department:
        def info(self):
            print("department working")

co = Company("Tech inc")
co.dep.info()


print("done")
