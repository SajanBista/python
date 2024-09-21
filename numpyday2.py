"""filling arrays with specific values
import numpy as np
print(np.zeros(5))
print(np.ones(20))
print(np.full((4,5),13))
print(np.full((2,2),11))

#creating array for range
#creating integer range with arange

import numpy as np
print(np.arange(5))
print(np.arange(5,10))
print(np.arange(10,1,-2),np.arange(12,4,-3))

#creating floating point range with l inspace

import numpy as np
print(np.linspace(.2,1.2,num=8))

#reshaping array
print(np.arange(1,21).reshape(2,10))

#displaying large array
import numpy as np
print(np.arange(1,100001).reshape(4,25000))

#small task
#use numpy function arange to create an array of 20 even integers from 2 through 40,then reshape the result into a 4-by-5 shape
import numpy as np
print(np.arange(2,41,2).reshape(4,5))"""


