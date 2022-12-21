import src.module_equations.inverse_mtr as inv

a = [[1, 2, 3], [4, 3, 3], [2, -1, 1]]
b = [[1], [-0.3], [8]]
print("\nThe matrix of the equation coefficients:", a, "The matrix of the equation constant terms:", b)
print("Get the solution using inverse_matrix_method():", inv.inverse_matrix_method(a, b))
print("a and b were not changed:", "\ta:", a, "\tb:", b, "\n")

print("Get identity matrix with 4 rows and columns:", inv.get_identity(4))

c = [[1, 0, 0, 3, 2, 5], [0, 1, 0, 4, 0.3, -4.001], [0, 0, 1, 2, 3, 18.4]]
print("\nSuppose, we have a c matrix, eliminated by Gauss-Jordan method, c:", c)
print("Extract inverse matrix from c", inv.extract(c), "\tc:", c)

d = [[3, 2, 5], [4, 0.3, -8], [2, 3, 0.1]]
print("\nThere's a matrix d:", d)
print("Get the inverse matrix for d", inv.inverse(d), "\td:", d)
