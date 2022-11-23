import src.module_matrix.matrix as mtr


a = [[1, 2, -3], [3, 4, 0], [3, 2, 4]]
b = [[2, 1, 1], [0, 1, 1], [5, -1, 1]]
print("Initial matrices:\t", "a:", a, "\t", "b:", b, end="\n\n")
print("Sum:", mtr.matrix_sum(a, b), "\ta:", a)
print("Diff:", mtr.matrix_diff(a, b), "\ta:", a)
print("Transpose:", mtr.matrixT(a), "\ta:", a)
print("Scalar multiplication (by 5):", mtr.matrix_scalar_mlt(a, 5), "\ta:", a)
print("Scalar division (by 1): ", mtr.matrix_scalar_div(a, 1), "\ta:", a)
print("Matrix multiplication:", mtr.matrix_mltp(a, b), "\ta:", a)
print("Get row:", mtr.getRow(a, 1), "\ta:", a)
print("Get column:", mtr.getCol(a, 1), "\ta:", a)
print("Swap rows:", mtr.swapRows(a, 0, 2), "\ta:", a)
print("The 2 row times 3:", mtr.row_times_scl(a, 1, 3, do_copy=False), "\ta:", a)
print("The 1 row divided by 2:", mtr.row_div_scl(a, 0, 2), "\ta:", a)

c = [[1, 2, 3, 4, 0], [7, 8, 5, 2, 1], [1, 0, 0, 0, 0], [2, 1, 1, 1, 1]]
print("Elementary operation: ", mtr.sum_rows(c, 3, 2, 2, 3), "\tc:", c)

k = [[1, 2, 3], [3, 2, 1]]
d = [[1.00000000009, 2, 3], [3, 2.00000000000011, 1]]
print("k:", k, "\td:", d, "\nCheck if k and d are almost equal:", mtr.mtr_are_almost_equal(k, d))
