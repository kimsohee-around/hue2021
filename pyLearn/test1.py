print("hello python  ")
"""
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
"""
x = 5
y = "John"
print(type(x))
print(type(y))
#x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
#fruits = ["apple", "banana", "cherry"]
#x, y, z = fruits
print(x)
print(y)
print(z)
x = 5
y = "John"
#print(x + y)  #TypeError: unsupported operand type(s) for +: 'int' and 'str'

x = "awesome"
def myfunc():
    #global x
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)