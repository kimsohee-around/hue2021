thislist =["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)
#You can also customize you own function by using the keyword argument key = function.
#The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)   #if you want a case-insensitive sort function
print(thislist)
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, 
#and changes made in list1 will automatically also be made in list2.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
#mylist=list(thislist)

thislist[1]="mango"
print(mylist)
print(thislist)
#
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
for x in list2:
    list1.append(x)

print(list1)
#
list1.extend(list2)
print(list1)
#list method : https://www.w3schools.com/python/python_lists_methods.asp
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items can be of any data type:
#A tuple can contain different data types:
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#You can access tuple items by referring to the index number, inside square brackets:
#To determine if a specified item is present in a tuple use the in keyword:
'''
Once a tuple is created, you cannot change its values. 
Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, 
change the list, and convert the list back cinto a tuple.
'''
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)  #or y.remove("apple") ,y.append("orange")
print(x)
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
#When we create a tuple, we normally assign values to it. 
#This is called "packing" a tuple:
#we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits   #Assign the rest of the values as a list called "red":
(green, *tropic, red) = fruits

#
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
for i in range(len(thistuple)):
    print(thistuple[i])
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
mytuple = fruits * 3

print(mytuple)
#Python has two built-in methods that you can use on tuples. : count(), index()
