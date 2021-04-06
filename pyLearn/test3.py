x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
#Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1, 10))
#You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = "Hello, World!"
print(a[1])
#Loop through the letters in the word "banana":
for x in "banana":
    print(x)
print(len(a))
txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
    print("있다.")
if "expensive" not in txt:
    print("싸다")
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
print(a.upper())
print(a.lower())
print(a.strip()) # a "Hello, World!  " returns "Hello, World!"
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']
#we can combine strings and numbers by using the format() method!
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#All string methods returns new values. 
#They do not change the original string.
#https://www.w3schools.com/python/python_strings_methods.asp
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
print(bool("Hello"))
print(bool(15))
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print(bool(0))
x = 200
print(isinstance(x, int))
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))