import numpy
from scipy import stats
import matplotlib.pyplot as plt

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 40)

print(x)

speed = [32,111,138,28,59,77,97]

#mean: Độ lệch chuẩn
std = numpy.std(speed)

#var:để tìm phương sai:
var = numpy.var(speed)

#mean: để tìm tốc độ trung bình:
mean = numpy.mean(speed)

#median: để tìm giá trị ở giữa:
median = numpy.median(speed)

#mode: để tìm số xuất hiện nhiều nhất:
mode = stats.mode(ages)


print(std)
print(var)
print(mean)
print(median)
print(mode)

# create list random
random = numpy.random.uniform(0, 5, 100)

print(random)

# draw: Data Distribution
values = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(values, 100)
plt.show()

# draw: Normal Data Distribution
value = numpy.random.normal(8.0, 1.0, 100000)
plt.hist(value, 100)
plt.show()

# Scatter Plot
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

# Linear Regression
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# du doan speed sau 15 nam 
speed = myfunc(10)
print(speed)

# Bad Fit?
x1 = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y1 = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x1, y1)

def myfunc2(x1):
  return slope * x1 + intercept

mymodel = list(map(myfunc2, x1))

plt.scatter(x1, y1)
plt.plot(x1, mymodel)
plt.show()


#Polynomial Regression
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()