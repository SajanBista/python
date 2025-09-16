import math
import numpy as np
x = int(input("Enter the number of datas  for finding the variance "))
datas =[]
for i in range(x):
    val = int(input(f"x {i+1}"))
    datas.append(val)
mean = np.mean(datas)

print(mean)
total = 0
n = x
print("finding the sample for now")
for i in datas:
    diff = i-mean
    total =+diff**2
variance_population = total/(n-1)
print(variance_population)

variance_sample = total/n
print(variance_sample)


