# ufunctions in python
"""try adding two list either 
a=[1,2,3,4]
b=[5,6,7,8]
c=[]
for i,j in zip(a,b):
    c.append(i+j)
print(c)

import numpy as np
c=np.add(a,b)
print(c)"""
"""creating my own ufunction"""
import numpy as np
def mul(x, y, z):# creating normal function
    return x*y*z
mul=np.frompyfunc(mul,3,1)# adding it with universal function
print(mul([2,3], [4,5], [6,7])) #printing result along with passing values


arr=np.array([2,3,4,5,9])
x=np.lcm.reduce(arr)
print(x)


print("6" *(2**2))
   