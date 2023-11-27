import numpy as np
print("SJC22MCA-2027 : Georgekutty Biju")
print("S3MCA")
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])
C = np.array([[13, 14],
              [15, 16]])
result = np.dot(np.dot(A, B), C)
print("Result of Matrix Multiplication (A * B * C):")
print(result)