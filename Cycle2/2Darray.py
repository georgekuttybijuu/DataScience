import numpy as np
print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of columns: "))
complex_array = np.empty((num_rows, num_columns), dtype=complex)
for i in range(num_rows):
    for j in range(num_columns):
        real_part = float(input(f"Enter the real part for element ({i}, {j}): "))
        imag_part = float(input(f"Enter the imaginary part for element ({i}, {j}): "))
        complex_array[i, j] = complex(real_part, imag_part)
print("2D Array:")
print(complex_array)
rows, columns = complex_array.shape
print(f"a. Number of rows: {rows}")
print(f"   Number of columns: {columns}")
dimensions = complex_array.ndim
print(f"b. Dimension of the array: {dimensions}")
reshaped_array = complex_array.reshape(num_columns, num_rows)
print("Reshaped Array (3x2):")
print(reshaped_array)
