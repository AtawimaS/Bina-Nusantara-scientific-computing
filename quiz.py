def gauss_seidel(A, b, x0, max_iter=100, tol=1e-6):
    n = len(A)
    x = x0.copy()  # Menggunakan salinan tebakan awal untuk menghindari perubahan nilai asli

    for k in range(max_iter):
        for i in range(n):
            sum_ax = 0
            for j in range(n):
                if j != i:
                    sum_ax += A[i][j] * x[j]

            x[i] = (b[i] - sum_ax) / A[i][i]

        error = max(abs(A @ x - b))  # Menghitung error dengan norma maksimum
        if error < tol:
            break

    return x


# Matriks koefisien A
A = [[17, 4, -3], [-7, -8, 5], [-3, 12, 7]]

# hasil b
b = [33, 23, -13]

x0 = [0, 0, 0]

# Panggil fungsi Gauss-Seidel
solution = gauss_seidel(A, b, x0)

# Cetak solusi
print("Solusi:")
for i, x in enumerate(solution):
    print(f"x{i+1} = {x}")
