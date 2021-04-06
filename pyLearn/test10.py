class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass
x = Student("Mike", "Olsen")
x.printname()

class Student2(Person):
    def __init__(self, fname, lname,year):
        Person.__init__(self, fname, lname)
        #super().__init__(fname, lname)
        self.graduationyear = 2019
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student2("Mike", "Olsen", 2019)
x.welcome()
print(x.graduationyear)

#An iterator is an object that contains a countable number of values.
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#an iterator is an object which implements the iterator protocol
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#We can also use a for loop to iterate through an iterable object:
'''
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.
'''
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

'''
To prevent the iteration to go on forever, we can use the StopIteration statement.
In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
'''
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers2()
myiter = iter(myclass)

for x in myiter:
    print(x)




