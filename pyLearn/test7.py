#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is unordered, changeable and does not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"]) #x = thisdict.get("model")
print(len(thisdict))
#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))
x = thisdict.get("model")
x = thisdict.keys()  #dict_keys(['brand', 'model', 'year'])
print(x) #after the change
x = thisdict.values() #dict_values(['Ford', 'Mustang', 2020])
print(x) #after the change
x = thisdict.items()
print(x) #after the change
thisdict["color"] = "white"
print(x) #after the change

thisdict["year"] = 2020
print(x) #after the change
#
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
#To determine if a specified key is present in a dictionary use the in keyword:
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
    
#
thisdict.update({"year": 2020}) #The argument must be a dictionary, or an iterable object with key:value pairs.

car.pop("model")
print(car)

thisdict.popitem() #removes the last inserted item
print(thisdict)
del thisdict["model"]  #removes the item with the specified key name:
#del thisdict  #"thisdict" no longer exists.
#clear() method empties the dictionary:

for x in thisdict:
    print(x)  #all key names
for x in thisdict:
    print(thisdict[x])  #all values
for x in thisdict.values():
    print(x)
for x in thisdict.keys():
    print(x)
for x, y in thisdict.items():
    print(x, y)

mydict = thisdict.copy()
print(mydict)
mydict2 = dict(thisdict)
print(mydict2)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
#https://www.w3schools.com/python/python_dictionaries_methods.asp
a = 33
b = 200
if b > a:
    print("b is greater than a")
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
    
# short hands #
print("A") if a > b else print("B") #Ternary Operators, or Conditional Expressions.
a = 330
b = 33
print("A") if a > b else print("=") if a == b else print("B")
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
#if you for some reason have an if statement with no content,
if b > a:
    pass

i = 1
while i < 6:
    print(i)
    if i == 3:
            break  #continue
    i += 1
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
for x in range(6):  #the values 0 to 5.
    print(x)
for x in range(2, 6):
    print(x)
for x in range(2, 30, 3):
    print(x)
for x in range(6):
    print(x)
else:
    print("Finally finished!")
    
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
#or some reason have a for loop with no content,
for x in [0, 1, 2]:
    pass  
