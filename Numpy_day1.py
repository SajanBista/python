#Create 5*5 matrix

import numpy as np
np.random.seed(42)
matrix = np.random.randint(1,101,(4,4))
print(matrix)

mean = np.mean(matrix)
median = np.median(matrix)
#mode = np.mode(matrix)
standard_deviation = np.std(matrix)

print("mode\n", mean)
print("median\n",median)
#print("mode\n", mode)
print("standard deviation", standard_deviation)

modify_matrix = np.where(matrix>mean,1,0)

print(modify_matrix)