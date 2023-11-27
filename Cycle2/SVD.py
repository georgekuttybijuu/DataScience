import numpy as np
print("SJC22MCA-2027 : Georgekutty Biju")
print("S3MCA")
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
U, S, Vt = np.linalg.svd(A)
A_hat = U @ np.diag(S) @ Vt
print("Original Matrix A:")
print(A)
print("\nSingular Values:")
print(S)
print("\nReconstructed Matrix A_hat:")
print(A_hat)