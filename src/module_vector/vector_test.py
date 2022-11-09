import vector as vc
from vector import scalars_are_almost_eq, vec_are_almost_eq


def test_vsum():
    a = [1, 3, 9]
    b = [1, 2, 0]
    exp = [2, 5, 9]
    res = vc.vsum(a, b)
    assert vec_are_almost_eq(exp, res)


def test_vdiff():
    a = [1, 3, 9]
    b = [1, 2, 0]
    exp = [0, 1, 9]
    res = vc.vdiff(a, b)
    assert vec_are_almost_eq(exp, res)


def test_vec_scal_prod():
    a = [1, 3, 9]
    b = 10
    exp = [10, 30, 90]
    res = vc.vec_scal_prod(a, b)
    assert vec_are_almost_eq(exp, res)


def test_vec_scal_div():
    a = [1, 3, 9]
    b = 10
    exp = [0.1, 0.3, 0.9]
    res = vc.vec_scal_div(a, b)
    assert vec_are_almost_eq(exp, res)


def test_mgn():
    a = [3, 4]
    exp = 5
    res = vc.mgn(a)
    assert scalars_are_almost_eq(exp, res)


def test_dot_product():
    a = [1, 3, 9]
    b = [1, 2, 0]
    exp = 7
    res = vc.dot_product(a, b)
    assert scalars_are_almost_eq(exp, res)


def test_cosine():
    a = [2, 0]
    b = [-5, 0]
    exp = -1
    res = vc.cosine(a, b)
    assert scalars_are_almost_eq(exp, res)


def test_angle_rad():
    a = [7, 0]
    b = [4, 0]
    exp = 0
    res = vc.angle_rad(a, b)
    assert scalars_are_almost_eq(exp, res)


def test_angle_grad():
    a = [-7, 0]
    b = [4, 0]
    exp = 180
    res = vc.angle_grad(a, b)
    assert scalars_are_almost_eq(exp, res)


def test_reversed_vec():
    a = [8, -12]
    exp = [-8, 12]
    res = vc.reversed_vec(a)
    assert vec_are_almost_eq(exp, res)


def test_collinear():
    a = [2, 2]
    b = [3, 3]
    exp = True
    res = vc.collinear(a, b)
    assert exp == res


def test_parallel():
    a = [2, 1]
    b = [4, 2]
    exp = True
    res = vc.parallel(a, b)
    assert exp == res


def test_opposite():
    a = [2, 1]
    b = [-4, -2]
    exp = True
    res = vc.opposite(a, b)
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
    res = vc.equal(a, b)
    assert exp == res


def test_ort():
    a = [0, 2]
    b = [4, 0]
    exp = True
    res = vc.ort(a, b)
    assert exp == res


def test_norm():
    a = [3, 4]
    exp = [0.6, 0.8]
    res = vc.norm(a)
    assert vec_are_almost_eq(exp, res)


def test_proj():
    a = [2, 2]
    b = [3, 0]
    exp = 2
    res = vc.proj(a, b)
    assert scalars_are_almost_eq(exp, res)


def test_vproj():
    a = [-2, 2]
    b = [4, 0]
    exp = [-2.0, 0.0]
    res = vc.vproj(a, b)
    assert vec_are_almost_eq(exp, res)
