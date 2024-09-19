"""1)single dimensional arguments

import numpy as np
numbers= np.array([2,3,4,5,6])
type(numbers)
numbers
print(numbers)"""

"""2.multidimensional arguments

import numpy as np

arr = np.array([[1,3,4,5,],[2,5,6,7]])
print(arr)"""

"""3.create one dimensional array from a list comprehension that produces the  even integers from 2 through 20

import numpy as  np
arr=np.array([[x for x in range(2,21,2)],[x for x in range(2,21,2)]])
print(arr)
"""

"""4.create a 2-by-5 array containing the even integer from 2 through 10 in the first row and the 
odd integers from 1 through 9 in second row

import numpy as np
arr= np.array([[x for x in range(2,10,2)],[x for x in range(1,9,2)]])

print(arr)
"""
import numpy as np
arr= np.array([[x for x in range(2,10,2)],[x for x in range(1,9,2)]])
print(arr)