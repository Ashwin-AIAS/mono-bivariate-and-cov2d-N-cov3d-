from random import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# FILL THIS FUNCTION
def mean(values):
    mu = 0
    if len(values) == 0:
        return 0
    mu = sum(values) / float(len(values))
    return mu
    
# FILL THIS FUNCTION
def variance(values):
    sigma2 = 0
    n = len(values)
    if n <= 1:
        return 0.0
    mu = mean(values)
    ss = 0.0
    for v in values:
        diff = v - mu
        ss += diff * diff
    sigma2 = ss / float(n - 1)
    return sigma2
    
# FILL THIS FUNCTION
def covariance(values1, values2):
    assert(len(values1) == len(values2))
    cov = 0
    n = len(values1)
    if n <= 1:
        return 0.0
    mu1 = mean(values1)
    mu2 = mean(values2)
    ss = 0.0
    for x, y in zip(values1, values2):
        ss += (x - mu1) * (y - mu2)
    cov = ss / float(n - 1)
    return cov
    
# FILL THIS FUNCTION
def correlation_coefficient(values1, values2):
    assert(len(values1) == len(values2))
    corr = 0
    cov = covariance(values1, values2)
    sigma1 = sqrt(variance(values1))
    sigma2 = sqrt(variance(values2))
    if sigma1 == 0 or sigma2 == 0:
        return 0.0
    corr = cov / (sigma1 * sigma2)
    return corr

# Create some data
values1 = []
values2 = []
for i in range(10):
    values1.append(randint(-5, 20))
# This is creating simple correlated data
# If you want uncorrelated, comment this out and uncomment the next block
for v in values1:
    values2.append(v+randint(-1,20))
#for i in range(10):
#    values2.append(randint(-1,20))

# Compute -- this is calling your functions
mu1 = mean(values1)
sigma21 = variance(values1)
sigma1 = sqrt(sigma21)

mu2 = mean(values2)
sigma22 = variance(values2)
sigma2 = sqrt(sigma22)

cov = covariance(values1, values2)
corr = correlation_coefficient(values1, values2)

# Output some text...
print("Values 1:  ", values1)
print("Mean 1:    ", mu1)
print("Variance 1:", sigma21)
print("Std Dev 1: ", sigma1)
print("Values 2:  ", values2)
print("Mean 2:    ", mu2)
print("Variance 2:", sigma22)
print("Std Dev 2: ", sigma2)
print("Covariance:", cov)
print("Correlation Coefficent:", corr)

# ...and plot.
# First figure out the min and max for the x axis...
maxval = max([mu1+3*sigma1, mu2+3*sigma2])
minval = min([mu1-3*sigma1, mu2-3*sigma2])
# Plot the individual values...
for v in values1:
    plt.plot(v, 0, "ro")
for v in values2:
    plt.plot(v, 0, "bo")
# build a linear space by dividing maxval-minval by accuracy 100...
x = np.linspace(maxval, minval, 100)
# plot the normal distributions from (mu1,sigma1), (mu2,sigma2), and
# (mu1+mu2/2, cov)
plt.plot(x, stats.norm.pdf(x, mu1, sigma1), label="dist2", color="r")
plt.plot(x, stats.norm.pdf(x, mu2, sigma2), label="dist2", color="b")
plt.plot(x, stats.norm.pdf(x, (mu1+mu2)/2, sqrt(cov)), label="cov", color="g")

plt.legend()
plt.show()
