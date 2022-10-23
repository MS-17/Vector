from src import vector
from src.vector import scalars_are_almost_eq, vec_are_almost_eq


def test_vsum():
    a = [1, 3, 9]
    b = [1, 2, 0]
    exp = [2, 5, 9]
    res = vector.vsum(a, b)
    assert vec_are_almost_eq(exp, res)


def test_vdiff():
    a = [1, 3, 9]
    b = [1, 2, 0]
    exp = [0, 1, 9]
    res = vector.vdiff(a, b)
    assert vec_are_almost_eq(exp, res)


def test_vec_scal_prod():
    a = [1, 3, 9]
    b = 10
    exp = [10, 30, 90]
    res = vector.vec_scal_prod(a, b)
    assert vec_are_almost_eq(exp, res)


def test_vec_scal_div():
    a = [1, 3, 9]
    b = 10
    exp = [0.1, 0.3, 0.9]
    res = vector.vec_scal_div(a, b)
    assert vec_are_almost_eq(exp, res)


def test_mgn():
    a = [3, 4]
    exp = 5
    res = vector.mgn(a)
    assert scalars_are_almost_eq(exp, res)


def test_dot_product():
    a = [1, 3, 9]
    b = [1, 2, 0]
    exp = 7
    res = vector.dot_product(a, b)
    assert scalars_are_almost_eq(exp, res)


def test_cosine():
    a = [2, 0]
    b = [-5, 0]
    exp = -1
    res = vector.cosine(a, b)
    assert scalars_are_almost_eq(exp, res)


def test_angle_rad():
    a = [7, 0]
    b = [4, 0]
    exp = 0
    res = vector.angle_rad(a, b)
    assert scalars_are_almost_eq(exp, res)


def test_angle_grad():
    a = [-7, 0]
    b = [4, 0]
    exp = 180
    res = vector.angle_grad(a, b)
    assert scalars_are_almost_eq(exp, res)


def test_reversed_vec():
    a = [8, -12]
    exp = [-8, 12]
    res = vector.reversed_vec(a)
    assert vec_are_almost_eq(exp, res)


def test_collinear():
    a = [2, 2]
    b = [3, 3]
    exp = True
    res = vector.collinear(a, b)
    assert exp == res


def test_parallel():
    a = [2, 1]
    b = [4, 2]
    exp = True
    res = vector.parallel(a, b)
    assert exp == res


def test_opposite():
    a = [2, 1]
    b = [-4, -2]
    exp = True
    res = vector.opposite(a, b)
    assert exp == res


def test_scalars_are_almost_equal():
    a = 1
    b = 1.00000000000001
    exp = True
    res = scalars_are_almost_eq(a, b)
    assert exp == res


def test_vec_are_almost_equal():
    a = [1, 2]
    b = [1.00000000000001, 2.0000000000000002]
    exp = True
    res = vec_are_almost_eq(a, b)
    assert exp == res


def test_equal():
    a = [1, 8]
    b = [1, 8]
    exp = True
    res = vector.equal(a, b)
    assert exp == res


def test_ort():
    a = [0, 2]
    b = [4, 0]
    exp = True
    res = vector.ort(a, b)
    assert exp == res


def test_norm():
    a = [3, 4]
    exp = [0.6, 0.8]
    res = vector.norm(a)
    assert vec_are_almost_eq(exp, res)


def test_proj():
    a = [2, 2]
    b = [3, 0]
    exp = 2
    res = vector.proj(a, b)
    assert scalars_are_almost_eq(exp, res)


def test_vproj():
    a = [-2, 2]
    b = [4, 0]
    exp = [-2.0, 0.0]
    res = vector.vproj(a, b)
    assert vec_are_almost_eq(exp, res)
