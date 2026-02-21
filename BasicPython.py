# Subscript - the method of pulling out an element from a string.
name = "Raj"
print(name[0])

# Nested If else
height = int(input("Give in cm.."))
bill = 0
if height >= 120:
    print("eligible")
    age = int(input("Age pls.."))
    if age < 12:
        bill = 5
    elif age <=18:
        bill = 7
    else:
        bill = 10
    print(f"total bill {bill}")
else:
    print("not eligible")

# random data
import random
number = random.randint(1,10)
print(number)

# use lambda
my_list = [1,2,3]
f = lambda x:x**2
sq = map(f,my_list)
print(list(sq))

#highest number and second highest number
numbers = [78,89,22,90,55,23]
highest_number = 0
second_highest_number = 0
for n in numbers:
    if n > highest_number:
        highest_number = n
    elif n > second_highest_number and n !=highest_number:
        second_highest_number = n
print(highest_number)
print(second_highest_number)

#lowest number and second lowest number
numbers = [10,30,20,5,4,90,80,60]
lowest_number=numbers[0]
second_lowest_number=float('inf')
for i in numbers:
    if i < lowest_number:
        second_lowest_number = lowest_number
        lowest_number = i
    elif i < second_lowest_number and i != lowest_number:
        second_lowest_number = i
print(lowest_number)
print(second_lowest_number)

# Prime check
def primeCheck(number):
    is_prime = True
    for i in range(2,number):
        if number%i == 0:
            is_prime = False
    if is_prime:
        print("It's prime")
    else:
        print("It's not prime")
n = int(input("Enter number "))
primeCheck(number=n)

# Prime Check between numbers 
 def is_prime(num):
     is_prime = True
     for n in range(2, num):
         if num % n == 0:
             is_prime = False
     if is_prime:
         return num
         
def prime_numbers_between(n1, n2):
    prime_numbers = []
    for num in range(n1, n2 + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

n1 = int(input("Enter the starting number: "))
n2 = int(input("Enter the ending number: "))
prime_list = prime_numbers_between(n1, n2)
print("Prime numbers between", n1, "and", n2, "are:", prime_list)

# dictionary - It's a collection of data, which is stored as key-value pair. dictionaries are enclosed with curly braces.
# key cant be duplicated but values can
dict = {
    "QA" : "Quality Analyst",
    "Dev" : "Development"
}
for Key in dict:
    print(Key)
    print(dict[Key])

# Formatted name
def fomat_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "Please enter valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"name is {formatted_f_name} {formatted_l_name}"
print(fomat_name(input("Enter first name "), input("Enter last name ")))

# High order function - Calculator is a high order function because it's actually taking another function as an input
# and then working with it inside the body of the function
def add(n,m):
    return  n+m
def substract(n,m):
    return n-m
def calculator(n,m,func):
    return func(n,m)
result1 = calculator(5,6,add)
result2 = calculator(5,6,substract)
print(result1, result2)

# From turtle module import class Turtle. From that class make an object t
# Different object function is independent of each other. We can say that they are each a separate instances
# When user taps a specific key on keyboard & the code that allows us to do what user does, are called Event Listeners.
# '_' signifies that the loop variable is not actually needed or used within the loop block
import random
from turtle import Turtle
import turtle as t1
t = Turtle()
t1.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
t.speed("fastest")
for _ in range(5):
    t.color(random_color())
    t.forward(50)
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(40)
    t.left(72)

def spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading()+gap_size)
spirograph(5)
# Tuples - it's same like a list but once created value can't be modified.
piano_tuples = ["a","b","c","d","e","f","g"]
print(piano_tuples[2:5])
print(piano_tuples[2:])
print(piano_tuples[:5])
print(piano_tuples[2:5:2])
print(piano_tuples[::2])

# Open,read,write - To read,write,append to file, Use 'With' keyword and use different modes which is built in open() function.
with open("new_file.txt") as file:
    print(file.read())
with open("new_file.txt", mode="a") as file:
    file.write("\nthis is 2nd line")
with open("new_file.txt", mode="w") as file:
    file.write("this is 2nd line")

# list comprehension - It allows to generate a new list by iterating over an existing lists, tuples, strings and
# applying an expression to each element.
one_list = [1,2,3]
f1 = [x**2 for x in one_list]
print(f1)
f2 = [x**2 for x in one_list if x%2 == 0]
print(f2)

# Dictionary comprehension - same as list comprehension. But it generates dictionary instead of list
two_list = [1,2,3]
f3 = {x:x**2 for x in two_list}
print(f3)
f4 = {x:x**2 for x in two_list if x%2 == 0}
print(f4)

# Read csv
import pandas
data = pandas.read_csv("NewCsv - Sheet1.csv")
temp_list = data["temp"].to_list()
print(temp_list)
print(data["temp"].max())
# Dictionary using pandas
student_dictionary = {"student": ["Raj","Rahul","Rohit"], "score": [55,80,85]}
student_dataframe = pandas.DataFrame(student_dictionary)
print(student_dataframe)

# Many positional arguments - using *arg syntax we can define many positional arguments. args will use as tuples,
# containing all the positional arguments passed to the function
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(add(1,2,3,4))
# Keyword arguments - using **kwargs syntax we can pass an arbitary number of keyword arguments to a function
def cal(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
cal(2,add=3,multiply=5)

#Exceptions
# Try - Something that might cause an exception, If an exception occurs within this block, Python looks for an
# appropriate except block to handle it.
# Except - Do this if there is an exception, The except block is used to handle specific exceptions that occur
# within the try block.
# Else - Do this if there were no exception. The else block is executed if no exceptions are raised in the try block
# Finally - Do this whatever happens, It is executed after the try and except blocks, even if an exception was raised.
# Raise - Custom create exception
# if height > 3:
#     raise ValueError("this is not right")

class CustomError(Exception):
    pass
def divide(x, y):
    try:
        if y == 0:
            raise CustomError("Cannot divide by zero.")
        result = x / y
    except CustomError as e:
        print("Error:", e)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print("Division result:", result)
    finally:
        print("Cleanup: This will always be executed.")

# Read,Write JSON file
import json
with open("new_file.json") as file:
    print(json.load(file))
with open("new_file.json", "w") as file:
    json.dump({"c":3}, file)         # it will replace previous value

# API - It's a set of commands,functions,protocols and objects that programmers can use to create software or interact
# with an external system

# Composition - In composition one class acts as a container of other class. If you destroy container there is no
# existance of contents.
class Engine:
    def __init__(self, capacity):
        self.capacity = capacity
    def start(self):
        print("Engine started")
class Car:
    def __init__(self, capacity):
        self.engine = Engine(capacity)
    def start(self):
        print("Car started")
        self.engine.start()
my_car = Car(2)
my_car.start()  # This will start both the car and its engine.
# Aggregation - It's a form of composition where objects are loosely coupled.Here no objects owns another objects. It
# just creates references. If you destroy the container then content will still exist
class Engine:
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print("Engine started")
class Car:
    def __init__(self, engine):
        self.engine = engine
    def start(self):
        print("Car started")
        self.engine.start()
my_engine = Engine(2)
my_car = Car(my_engine)
my_car.start()  # This will start both the car and its engine.

# Shallow Copy - It creates new object but it doesn't create new copies of the nested objects. So, changes in the
# nested objects will affect the original
# Deep Copy - It creates new object and also creates new copies of nested objects within it. So, changes in the
# nested objects doesn't affect the original
import copy
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list3 = copy.copy(list1)
list3[0][0] = "a"
list4 = copy.deepcopy(list2)
list4[0][0] = "a"
print(list1, list3)
print(list2, list4)

# Fetch items from the iterator
my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)  # Create an iterator
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
for item in my_iterator:  # Iterating through the remaining elements
    print(item)  # Output: 3, then 4
# Permutation
def gn_pr(string,current=''):
    if len(string) == 0:
        print(current)
    else:
        for char in string:
            new_string=string.replace(char,'',1)
            gn_pr(new_string,current+char)

string="abcd"
gn_pr(string)

from itertools import permutations
s = "abcd"
perms = [''.join(p) for p in permutations(s)]
for perm in perms:
    print(perm)

# input "aaaabbbbbcccdddd" output a4b5c3d4
def compress(string):
    new_string=''
    count=1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            new_string += string[i] + str(count)
            count = 1
    new_string += string[-1] + str(count)
    return new_string

print(compress("aaaabbbbbcccdddd"))

# Fabonucci
def fab(n):
    if n <= 1:
        return n
    else:
        return fab(n-1)+fab(n-2)
print([fab(i) for i in range(10)])

#Ana gram
words = ["listen", "silent", "enlist", "inlets", "tinsel", "banana", "bbnnaa", "apple", "papel", "baker"]
anagram_map = {}
for word in words:
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagram_map:
        anagram_map[sorted_word].append(word)
    else:
        anagram_map[sorted_word] = [word]
anagram_list = [ana for ana in anagram_map.values()]
print(anagram_list)

