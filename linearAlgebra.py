import numpy as np
A = np.array([[4, 7], [2, 6]])
b = np.array([10, 5])
x = np.linalg.solve(A, b)
print("Solution x:", x)

det_A = np.linalg.det(A)
print("Determinant of A:", det_A)


eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

from scipy.sparse import csr_matrix

# Creating a sparse matrix
sparse_matrix = csr_matrix([[1, 0, 0], [0, 0, 2], [0, 3, 0]])
print("Sparse matrix:\n", sparse_matrix)


dense_matrix = sparse_matrix.toarray()
print("Dense matrix:\n", dense_matrix)

B = csr_matrix([[0, 5, 0], [0, 0, 0], [7, 0, 0]])
C = sparse_matrix + B
print("Sparse matrix addition:\n", C.toarray())


D = sparse_matrix @ B.T  # Matrix multiplication
print("Sparse matrix multiplication:\n", D.toarray())

from scipy.sparse.linalg import spsolve
from scipy.sparse import csc_matrix

A_sparse = csc_matrix([[3, 0, 2], [0, 4, 0], [1, 0, 5]])
b = np.array([2, 4, 6])

x = spsolve(A_sparse, b)
print("Solution to Ax = b:", x)

# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])
# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]
# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])


# Sort temperatures_ind by index values
print(temperatures_ind.sort_index(ascending=[True]))

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending=[True, False]))