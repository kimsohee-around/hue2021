#  defined using the def keyword
def my_function0():
    print("Hello from a function")

# To call a function
my_function0()

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
'''
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
'''
def my_function2(fname, lname):
    print(fname + " " + lname)

my_function2("Emil", "Refsnes")

#how many arguments that will be passed into your function
def my_function3(*kids):
    print("The youngest child is " + kids[2])

my_function3("Emil", "Tobias", "Linus")

#send arguments with the key = value syntax.
def my_function4(child3, child2, child1):
    print("The youngest child is " + child3)

my_function4(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#do not know how many keyword arguments that will be passed into your function
def my_function5(**kid):
    print("His last name is " + kid["lname"])

my_function5(fname = "Tobias", lname = "Refsnes")

#use a default parameter value.
def my_function6(country = "Norway"):
    print("I am from " + country)

my_function6("Sweden")
my_function6("India")
my_function6()
my_function6("Brazil")

def my_function7(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function7(fruits)


