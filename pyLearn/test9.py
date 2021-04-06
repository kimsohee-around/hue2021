def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction2():
    pass

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(k,result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#A lambda function is a small anonymous function.only have one expression.
# lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
#Use lambda functions when an anonymous function is required for a short period of time.

class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

#All classes have a function called __init__(), 
#which is always executed when the class is being initiated.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()
'''
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belong to the class.
It does not have to be named self , you can call it whatever you like, 
but it has to be the first parameter of any function in the class:
'''
#Delete the age property from the p1 object:
del p1.age
print(p1.age)#오류
del p1  #Delete the p1 object:
#class definition with no content
class Person2:
    pass

#
import mymodule
mymodule.greeting("Ren")

