import numpy as np
def is_symmetric(matrix):
    transpose = np.transpose(matrix)
    return np.array_equal(matrix, transpose)
def is_skew_symmetric(matrix):
    transpose = np.transpose(matrix)
    return np.array_equal(matrix, -transpose)
# Input the dimensions of the matrix
print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
# Initialize an empty matrix
matrix = []
# Input the matrix elements
print("Enter the matrix elements row by row:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)

matrix = np.array(matrix)
if is_symmetric(matrix):
    print("The matrix is symmetric.")
elif is_skew_symmetric(matrix):
    print("The matrix is skew-symmetric (antisymmetric).")
else:
    print("The matrix is neither symmetric nor skew-symmetric.")
