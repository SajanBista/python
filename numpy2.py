import numpy as np
#Generate a 5x5 Matrix with Random Integers
arr=np.random.randint(10,100,(5,5))

#Convert an array into a range of 0 to 1 using min-max normalization.
Normalized_array = (arr-arr.min())/(arr.max()-arr.min())
print(Normalized_array)

#Extract unique values from an array and count their occurrences.
unique_values, counts = np.unique(arr, return_counts=True)

print("unique_values: ", unique_values)
print("counts: ",counts )

#Stack Two Arrays Vertically & Horizontally
print(arr)
arr2=np.transpose(arr)
print(arr2)

vstack = np.vstack((arr,arr2))
hstake = np.hstack((arr,arr2))

print(vstack)
print(hstake)

#Replace Values Based on a Condition
arr = np.where(arr>50,50,arr)

print(arr)

#Find the Determinant & Inverse of a Matrix
determinant = np.linalg.det(arr)

print(determinant)

if determinant !=0:
    inverse_matrix =np.linalg.inv(arr)
else:
    inverse_matrix ="determinant is 0 so it doesn't exist".capitalize

print(inverse_matrix)

#Apply a Custom Function to Each Element
result = arr**2 + 1
print(result)