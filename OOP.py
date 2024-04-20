# Inheritance
class Animal:
    def __init__(self):
        self.eyes = 2
    def breathe(self):
        print("x,y")
class Bird(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("a,z")
n = Bird()
n.breathe()
print(n.eyes)
# Bird class is inheriting from Animal class. Inside init we add super().__init__(). where all the attributes and
# methods are inheriting from Animal class. super refers to superclass.Create object n that's created from Bird class.

# Polymorphism
String = "Hello World"
List = [1,2,3,5]
print(len(String))
print(len(List))
# Len function is used for different types like string and list

# OverWriting
def f(x):
    return x+3
print(f(3))
def f(x):
    return x+4
print(f(3))
# Once overwrite a function, original function will be gone.

# Override
class Animal:
    def walk(self):
        print("Parent clss")
class Dog(Animal):
    def walk(self):
        print("Child class")
r = Animal() # Invoke parent class through object r
r.walk()
r = Dog() # Invoke child class through object r
r.walk()

# Dundee or magic method
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person named {self.name}"
Person1 = Person("Raj")
print(Person1)

# Recurtion
def factorial(n):
    if n == 0:                      # Base case: if n is 0, return 1
        return 1
    else:
        return n * factorial(n-1)   # Recursive case: n! = n * (n-1)!
print(factorial(5))                 # Output: 120
