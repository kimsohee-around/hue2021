# import matplotlib.pyplot as plt
# 
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]   #age
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]  #speed
# 
# plt.scatter(x, y)
# plt.show()
# 
# import numpy
# x = numpy.random.normal(5.0, 1.0, 1000)
# y = numpy.random.normal(10.0, 2.0, 1000)
# #We can see that the dots are concentrated around the value 5 on the x-axis, and 10 on the y-axis.
# plt.scatter(x, y)
# plt.show()

#Linear regression uses the relationship 
#between the data-points to draw a straight line through all them.
#This line can be used to predict future values

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

print(slope)
print(intercept)
print(r)    #-0.7585915243761551
print(p)
print(std_err)
speed = myfunc(10)    #The example predicted a speed at 85.6, which we also could read from the diagram:
print(speed)
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)   #0.013318141542974947
#The result: 0.013 indicates a very bad relationship, and tells us that this data set is not suitable for linear regression.

#Polynomial regression, 
#like linear regression, uses the relationship between the variables x and y to find the best way to draw a line through the data points.
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(x, y)
plt.show()

import numpy
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(1, 22, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

