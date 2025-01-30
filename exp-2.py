import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:\n", array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", array_2d)

# Create an array of zeros
zeros = np.zeros((2, 3))
print("\nArray of zeros:\n", zeros)

# Create an array of ones
ones = np.ones((3, 2))
print("\nArray of ones:\n", ones)

# Create an array using arange
arange_array = np.arange(0, 10, 2)
print("\nArray using arange:\n", arange_array)

# Indexing
print("\nElement at index 1 (1D):", array_1d[1])
print("Element at (0, 1) (2D):", array_2d[0, 1])

# Slicing
print("\nSlice 1D Array [1:4]:", array_1d[1:4])
print("Slice 2D Array [0:2, 1:3]:\n", array_2d[0:2, 1:3])

# Boolean indexing
bool_index = array_1d > 2
print("\nBoolean Indexing (values > 2):\n", array_1d[bool_index])

# Element-wise operations
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print("\nAddition:", array_a + array_b)
print("Subtraction:", array_a - array_b)
print("Multiplication:", array_a * array_b)
print("Division:", array_a / array_b)

# Statistical operations
print("\nSum:", array_a.sum())
print("Mean:", array_a.mean())
print("Standard Deviation:", array_a.std())

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
matrix_product = np.dot(matrix_a, matrix_b)
print("\nMatrix Multiplication:\n", matrix_product)

# Transpose
matrix_transpose = matrix_a.T
print("\nTranspose of matrix_a:\n", matrix_transpose)

import matplotlib.pyplot as plt

# Random array (uniform distribution)
random_uniform = np.random.rand(100)

# Random integers
random_integers = np.random.randint(0, 50, size=10)
print("\nRandom Integers:\n", random_integers)

# Plot histogram
plt.hist(random_uniform, bins=10, color="blue", alpha=0.7)
plt.title("Histogram of Uniform Distribution")
plt.show()

# Determinant
matrix_c = np.array([[3, 1], [2, 4]])
det = np.linalg.det(matrix_c)
print("\nDeterminant of matrix_c:", det)

# Solving linear equations (Ax = B)
A = np.array([[2, 1], [1, -1]])
B = np.array([3, 0])
x = np.linalg.solve(A, B)
print("\nSolution to linear equations (Ax = B):\n", x)

array_x = np.array([1, 2, 3, 4, 5])
array_y = np.array([5, 4, 3, 2, 1])

# Correlation
correlation = np.corrcoef(array_x, array_y)[0, 1]
print("\nCorrelation between arrays:", correlation)

# Covariance
covariance = np.cov(array_x, array_y)[0, 1]
print("Covariance between arrays:", covariance)

# Sorting
unsorted_array = np.array([5, 3, 8, 1, 2])
sorted_array = np.sort(unsorted_array)
print("\nSorted Array:", sorted_array)

# Searching
threshold = 4
filtered_elements = unsorted_array[unsorted_array > threshold]
print("Elements greater than", threshold, ":", filtered_elements)
