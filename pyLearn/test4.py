#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary,
# all with different qualities and usage.
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)
thislist = list(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thislist)
'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.
'''
#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
thislist = ["apple", "banana", "cherry"]
thislist[1] = ["blackcurrant", "watermelon"]
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#The extend() method does not have to append lists, 
#you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist.remove("banana")
thislist.pop(1) #If you do not specify the index, the pop() method removes the last item
del thislist[0]
#del thislist            #Delete the entire list:
#The clear() method empties the list.
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
[print(x) for x in thislist]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits]
#The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]
