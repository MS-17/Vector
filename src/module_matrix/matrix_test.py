import matrix as mtr
import src.module_vector.vector as vc


def test_matrix_sum():
    a = [[1, -8], [3, 1]]
    b = [[0, 17], [2, 1.5]]
    exp = [[1, 9], [5, 2.5]]
    res = mtr.matrix_sum(a, b)
    assert mtr.mtr_are_almost_equal(res, exp)


def test_matrix_diff():
    a = [[1, -8], [3, 1]]
    b = [[0, 17], [2, 1.5]]
    exp = [[1, -25], [1, -0.5]]
    res = mtr.matrix_diff(a, b)
    assert mtr.mtr_are_almost_equal(res, exp)


def test_matrixT():
    a = [[1, -8, 3], [3, 1, 4]]
    exp = [[1, 3], [-8, 1], [3, 4]]
    res = mtr.matrixT(a)
    assert mtr.mtr_are_almost_equal(res, exp)


def test_matrix_scalar_mlt():
    a = [[1, 2, 1], [19, 2, -9.1]]
    exp = [[3, 6, 3], [57, 6, -27.3]]
    res = mtr.matrix_scalar_mlt(a, 3)
    assert mtr.mtr_are_almost_equal(res, exp)


def test_matrix_scalar_div():
    a = [[1, 2, 1], [19, 2, -9.1]]
    exp = [[0.5, 1, 0.5], [9.5, 1, -4.55]]
    res = mtr.matrix_scalar_div(a, 2)
    assert mtr.mtr_are_almost_equal(res, exp)


def test_matrix_mlt():
    a = [[1, 2, 3], [2, 1, 1]]
    b = [[2], [2.5], [0]]
    exp = [[7], [6.5]]
    res = mtr.matrix_mltp(a, b)
    assert mtr.mtr_are_almost_equal(res, exp)


def test_getRow():
    a = [[1, 3, 4], [5, 2, -0.5]]
    exp = [5, 2, -0.5]
    res = mtr.getRow(a, 1)
    assert vc.vec_are_almost_eq(res, exp)


def test_getCol():
    a = [[1, 3, 4], [5, 2, -0.5]]
    exp = [3, 2]
    res = mtr.getCol(a, 1)
    assert vc.vec_are_almost_eq(res, exp)


def test_swapRows():
    a = [[1, 2, 3], [5, -1, 1], [1, 1.1, 1.2], [5, 3, -48848]]
    exp = [[1, 1.1, 1.2], [5, -1, 1], [1, 2, 3], [5, 3, -48848]]
    res = mtr.swapRows(a, 0, 2)
    assert mtr.mtr_are_almost_equal(res, exp)


def test_row_times_scl():
    a = [[5, 1, 1], [-1, 0, -3], [1, 100, 1000]]
    exp = [[5, 1, 1], [-1, 0, -3], [10, 1000, 10000]]
    res = mtr.row_times_scl(a, 2, 10)
    assert mtr.mtr_are_almost_equal(res, exp)


def test_row_div_scl():
    a = [[5, 1, 1], [-1, 0, -3], [1, 100, 1000]]
    exp = [[5, 1, 1], [-0.1, 0, -0.3], [1, 100, 1000]]
    res = mtr.row_div_scl(a, 1, 10)
    assert mtr.mtr_are_almost_equal(res, exp)


def test_sum_rows():
    a = [[1, 2, 3, 5], [2, 2, 2, 2], [1, 2, 1, 0], [3, 4, 0, 1]]
    exp = [[1, 2, 3, 5], [10, 12, 4, 6], [1, 2, 1, 0], [3, 4, 0, 1]]
    res = mtr.sum_rows(a, 1, 3, 2, 2)
    assert mtr.mtr_are_almost_equal(res, exp)


def test_mtr_are_almost_equal():
    a = [[1, 2, 3], [5, 4.0000000000009, 1]]
    b = [[1, 2, 3], [5, 4, 1.000000000003]]
    exp = True
    res = mtr.mtr_are_almost_equal(a, b)
    assert exp == res

