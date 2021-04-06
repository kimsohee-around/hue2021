import numpy
import matplotlib.pyplot as plt
'''
x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()
'''
#normal data distribution, or the Gaussian data distribution,
x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()


