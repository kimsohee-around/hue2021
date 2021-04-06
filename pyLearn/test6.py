#A set is a collection which is both unordered and unindexed(순서가없는)
#and do not allow duplicate values.
#Set items can be of any data type:A set can contain different data types:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
for x in thisset:
    print(x)
#Once a set is created, you cannot change its items, but you can add new items.
thisset.add("orange")
print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)
#update() method does not have be a set,
# it can be any iterable object (tuples, lists, dictionaries et,).
mylist = ["kiwi", "orange"]
thisset.update(mylist)
#If the item to remove does not exist, remove() will raise an error.
#If the item to remove does not exist, discard() will NOT raise an error.
#sets are unordered, so you will not know what item that gets removed.
#The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#clear() method empties the set:del keyword will delete the set completely:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
z = x.intersection(y)
print(x)
print(z)
x.symmetric_difference_update(y)
print(x)
z = x.symmetric_difference(y)
print(z)
#https://www.w3schools.com/python/python_sets_methods.asp