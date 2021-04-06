#Python 3.6 uses the input() method.
username = input("Enter username:")
print("Username is: " + username)
#Python 2.7 uses the raw_input() method.
#username = raw_input("Enter username:")

price = 49
txt = "The price is {} dollars"
print(txt.format(price))
txt = "The price is {:.2f} dollars"
print(txt.format(price))
#https://www.w3schools.com/python/ref_string_format.asp
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
'''
File Handling
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''
f = open("demofile.txt") # 같은 동작 : f = open("demofile.txt", "rt")
print(f.read())  #print(f.read(5))
#f = open("D:\\myfiles\welcome.txt", "r")
print(f.readline())   #Read one line of the file:
for x in f:
    print(x)
#
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#
f = open("demofile2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
# Create a file called "myfile.txt":
f = open("myfile.txt", "x")
f = open("demofile2.txt", "x") #??

import os
os.remove("demofile2.txt")

if os.path.exists("demofile.txt"):
    print("The file exists")
else:
    print("The file does not exist")
    
os.rmdir("myfolder")  #You can only remove empty folders.
