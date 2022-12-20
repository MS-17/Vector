import src.module_equations.linear_system as lns
from src.module_matrix.matrix import mtr_are_almost_equal
from src.module_vector.vector import  vec_are_almost_eq


def test_merge_mtr():
    a = [[5, 8, 2, 9], [3, 0, 1, 1], [2, 2, 2, 3]]
    b = [[1, 2], [8, 12], [-1, -1]]
    res = lns.merge_mtr(a, b)
    exp = [[5, 8, 2, 9, 1, 2], [3, 0, 1, 1, 8, 12], [2, 2, 2, 3, -1, -1]]
    assert res == exp


def test_move_forward_3d():
    a = [[1, 2, 4, 0], [3, 0, 1, 2], [5, 2, 4, 8]]
    res = lns.move_forward(a, True)
    exp = [[1, 2, 4, 0], [0, 1, 1.8333333333333333, -0.33333333333333], [0, 0, 1, -4.000000000000000000]]
    assert mtr_are_almost_equal(res, exp)


def test_move_backward_3d():
    a = [[1, 2, 3, 1], [0, 1, 2, 2], [0, 0, 1, 2]]
    res = lns.move_backward(a, True)
    exp = [[1, 0, 0, -1], [0, 1, 0, -2], [0, 0, 1, 2]]
    assert mtr_are_almost_equal(res, exp)


def test_gauss_3d():
    a = [[2, 3, 1, 0], [5, 3, 2, 2], [1, 1, 1, 2]]
    res = lns.gauss(a, True)
    exp = [[1, 0, 0, -0.4], [0, 1, 0, -0.8], [0, 0, 1, 3.2]]
    assert mtr_are_almost_equal(res, exp)


def test_get_solution_3d():
    a = [[3, 2, -1], [4, -3, 5], [0, 1, -2]]
    b = [[1], [6], [-5]]
    res = lns.get_solution(a, b)
    exp = [-1.06666666667, 4.4666666666667, 4.7333333333333]
    assert vec_are_almost_eq(res, exp)


def test_move_forward_2d():
    a = [[1, 2, 4], [3, -1, 1]]
    res = lns.move_forward(a, True)
    exp = [[1, 2, 4], [0, 1, 1.571428571428571428]]
    assert mtr_are_almost_equal(res, exp)


def test_move_backward_2d():
    a = [[1, -1.5, 3], [0, 1, -2]]
    res = lns.move_backward(a, True)
    exp = [[1, 0, 0], [0, 1, -2]]
    assert mtr_are_almost_equal(res, exp)


def test_gauss_2d():
    a = [[-4, 3, 0.2], [1, 0.4, -1.5]]
    res = lns.gauss(a, True)
    exp = [[1, 0, -0.9956521739130434], [0, 1, -1.2608695652173913]]
    assert mtr_are_almost_equal(res, exp)


def test_get_solution_2d():
    a = [[-0.4, 2], [0.01, -3]]
    b = [[-1.3], [3.6]]
    res = lns.get_solution(a, b)
    exp = [-2.79661016949152542, -1.209322033898305]
    assert vec_are_almost_eq(res, exp)
