'''
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy stands for Numerical Python.
'''

'''
In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
Arrays are very frequently used in data science, where speed and resources are very important.
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
'''
'''
By looking at the array, we can guess that the average value is probably around 80 or 90, 
and we are also able to determine the highest value and the lowest value, but what else can we do?
And by looking at the database we can see that the most popular color is white, and the oldest car is 17 years, 
but what if we could predict if a car had an AutoPass, just by looking at the other values?
That is what Machine Learning is for! Analyzing data and predicting the outcome!
In Machine Learning it is common to work with very large data sets. 
In this tutorial we will try to make it as easy as possible to understand the different concepts of machine learning, 
and we will work with small easy-to-understand data sets.
Mean - The average value
Median - The mid point value
Mode - The most common value
'''
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
print(x)
x = numpy.median(speed)
print(x)

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)

speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

speed = [32,111,138,28,59,77,97]
x = numpy.std(speed)
print(x)

x = numpy.var(speed)
print(x)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x)
'''
In the real world, the data sets are much bigger,
 but it can be difficult to gather real world data, at least at an early stage of a project.
How Can we Get Big Data Sets?
To create big data sets for testing, we use the Python module NumPy,
 which comes with a number of methods to create random data sets, of any size.
 '''
 
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)