import src.module_equations.inverse_mtr as inm
from src.module_matrix.matrix import mtr_are_almost_equal, matrix_mltp


def test_get_identity():
    length = 4
    res = inm.get_identity(length)
    exp = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    assert mtr_are_almost_equal(res, exp)


def test_extract():
    a = [[1, 0, 0, 3, 2, 5], [0, 1, 0, 4, 0.3, -4.001], [0, 0, 1, 2, 3, 18.4]]
    res = inm.extract(a)
    exp = [[3, 2, 5], [4, 0.3, -4.001], [2, 3, 18.4]]
    assert mtr_are_almost_equal(res, exp)


def test_inverse():
    a = [[3, 2, 5], [4, 0.3, -8], [2, 3, 0.1]]
    res = inm.inverse(a)
    exp = [[0.24955862498701838197, 0.15370235746183404299, -0.18174265240419565894],
           [-0.17031882853878907467, -0.10073735590403987952, 0.45695295461626337108],
           [0.11839235642330460069, -0.05192647211548447399, -0.073735590403987953063]]
    assert mtr_are_almost_equal(res, exp)


def test_inverse_matrix_method():
    a = [[1, 2, 3], [4, 3, 3], [2, -1, 1]]
    b = [[1], [-0.3], [8]]
    res = inm.inverse_matrix_method(a, b)
    exp = [[0.825], [-3.775], [2.575]]
    assert mtr_are_almost_equal(res, exp)


def test_inverse_matrix_method1():
    a = [[1, 2, 3], [4, 3, 3], [2, -1, 1]]
    b = [[1], [-0.3], [8]]
    res = inm.inverse_matrix_method(a, b)
    exp = matrix_mltp(a, res)
    assert mtr_are_almost_equal(b, exp)
