def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
    myinnerfunc()

myfunc()

x = 300
def myfunc2():
    print(x)

myfunc2()
print(x)

y = 300

def myfunc3():
    global z
    z=120
    y = 200
    print(y)

myfunc3()
print(y)
print(z)


import mymodule
mymodule.greeting("Ren")
print(mymodule.person1["name"])

import mymodule as mx
mx.greeting("choi")

import platform

x = platform.system()
print(x)
x=dir(platform)
print(x)
for y in x:
    print(y)    
from mymodule import person1

print (person1["age"])  #not mymodule.person1["age"]

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17) #Create a date object:

print(x)
print(x.strftime("%B"))

#A reference of all the legal format codes:
#https://www.w3schools.com/python/python_datetime.asp

'''
The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).


'''

import math

x = math.sqrt(64)

print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1
#https://www.w3schools.com/python/module_math.asp

'''
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
'''
#Convert from JSON to Python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# a Python object (dict):
x2 = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y2 = json.dumps(x2)

# the result is a JSON string:
print(x2)
print(y2)

#You can convert Python objects of the following types, into JSON strings:
'''
Python    JSON
dict    Object
list    Array
tuple    Array
str    String
int    Number
float    Number
True    true
False    false
None    null
'''

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x,indent=4))
json.dumps(x, indent=4, separators=(". ", " = "))
print(json.dumps(x,indent=4,sort_keys=True))
