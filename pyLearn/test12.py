#built-in package called re, which can be used to work with Regular Expressions.
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
'''
Function    Description
findall    Returns a list containing all matches
search    Returns a Match object if there is a match anywhere in the string
split    Returns a list where the string has been split at each match
sub    Replaces one or many matches with a string
'''

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)
#https://www.w3schools.com/python/python_regex.asp

x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
x = re.split("\s", txt)
print(x)

#You can control the number of occurrences by specifying the maxsplit parameter:
x = re.split("\s", txt, 1)
print(x)
x = re.sub("\s", "9", txt)
print(x)
#You can control the number of replacements by specifying the count parameter:
x = re.sub("\s", "9", txt, 2)
print(x)

'''
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
'''
#The regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)

'''
PIP is a package manager for Python packages, or modules if you like.
If you have Python version 3.4 or later, PIP is included by default.
 https://pypi.org/project/pip/
 Find Packages :Find more packages at https://pypi.org/.
'''

try:
  print(x)
except:
  print("An exception occurred")
  
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
try:
  print("Hello")
except:
  print("Something went wrong")
else:
    print("Nothing went wrong")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  #This can be useful to close objects and clean up resources:
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
#  
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

'''
The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.
'''