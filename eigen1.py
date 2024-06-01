import numpy as np
def normalize(x):
    fac = abs(x).max()
    x_n = x/ x.max()
    return fac, x_n
x = np.array([1,1,1])
A = np.array([[151, 146, 160, 166, 177, 188, 162, 168, 168],
              [77, 86, 116, 142, 148, 150, 142, 140, 123],
              [52, 74, 80, 89, 127, 111, 131, 127, 63],
              [65, 69, 95, 71, 97, 98, 104, 72, 48],
              [95, 50, 89, 68, 65, 59, 45, 55, 76],
              [95, 59, 88, 69, 33, 36, 40, 64, 94],
              [87, 73, 98, 76, 90, 90, 74, 58, 45],
              [69, 74, 78, 86, 136, 138, 137, 86, 44],
              [67, 74, 92, 98, 92, 107, 106, 132, 96]])
matrix_list = [A[i:i+3, j:j+3] for i in range(0, 9, 3) for j in range(0, 9, 3)]
eigenvalues_list = []
eigenvectors_list = []

for matrix in matrix_list:
    x = np.array([1,1,1])
    for i in range (8):
        x = np.dot(matrix,x)
        lambda_1,x=normalize(x)
    eigenvalues_list.append(lambda_1)
    eigenvectors_list.append(x)

for i, matrix in enumerate(matrix_list):
    print(f"Matrixatrix {i+1}:")
    print(f"Eigenvalues:\n{eigenvalues_list[i]}")
    print(f"Eigenvectors:\n{eigenvectors_list[i]}\n")
