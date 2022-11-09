import math as mth


def len_is_equal(a, b):
    """ Проверяет равны ли длины a и b """
    return len(a) == len(b)


def len_is_zero(vec1):
    """ Проверяет равна ли длина вектора 0 """
    if len_is_equal(vec1, []):
        raise ValueError("The vector length should not be equal to 0")
    return False


def check_len(vec1, vec2):
    """
    Проверяет равны ли длины данных векторов 0. Если да
    возвращает ValueError, если нет, то проверяет длины векторов на равенство
    """
    len_is_zero(vec1)
    len_is_zero(vec2)
    if not len_is_equal(vec1, vec2):
        raise ValueError("The lengths of the vectors are not equal!")


def vector_cpy(vec1, mkcpy=True):
    """ mkcpy=True -> сделать копию vec1, иначе -> вернуть vec1 """
    if mkcpy:
        result = vec1[:]
    else:
        result = vec1
    return result


def scalars_are_almost_eq(num1, num2, eps=1E-10):
    """ Проверяет числа на равенство с заданной точностью eps """
    return abs(num1 - num2) <= eps


def vec_are_almost_eq(vec1, vec2, eps=1E-10):
    """ Поэлементно проверяет координаты векторов на равенство с заданной точностью eps """
    check_len(vec1, vec2)
    eq = [scalars_are_almost_eq(i, j, eps) for i, j in zip(vec1, vec2)]
    return False not in eq


def vsum(vec1, vec2, mkcpy=True):
    """ Сумма векторов """
    check_len(vec1, vec2)
    result = vector_cpy(vec1, mkcpy)
    for i in range(len(result)):
        result[i] += vec2[i]
    return result


def vdiff(vec1, vec2, mkcpy=True):
    """ Разность векторов """
    check_len(vec1, vec2)
    result = vector_cpy(vec1, mkcpy)
    for i in range(len(result)):
        result[i] -= vec2[i]
    return result


def vec_scal_prod(vec1, scalar, mkcpy=True):
    """ Умножение вектора на число """
    result = vector_cpy(vec1, mkcpy)
    for i in range(len(result)):
        result[i] *= scalar
    return result


def vec_scal_div(vec1, scalar, mkcpy=True):
    """ Деление вектора на число """
    len_is_zero(vec1)
    if scalar == 0:
        raise ValueError("The scalar shouldn't be equal to 0!")
    return vec_scal_prod(vec1, 1 / scalar, mkcpy)


def mgn(vec1):
    """ mgn = magnitude, возвращает длину вектора """
    len_is_zero(vec1)
    sum1 = 0
    for i in vec1:
        sum1 += i * i
    return sum1 ** 0.5


def dot_product(vec1, vec2):
    """ Скалярное произведение """
    check_len(vec1, vec2)
    dot = 0
    for i in range(len(vec1)):
        dot += vec1[i] * vec2[i]
    return dot


def cosine(vec1, vec2):
    """ Косинус угла между векторами """
    check_len(vec1, vec2)
    return dot_product(vec1, vec2) / (mgn(vec1) * mgn(vec2))


def angle_rad(vec1, vec2):
    """ Угол между векторами в радианах """
    check_len(vec1, vec2)
    return mth.acos(cosine(vec1, vec2))


def angle_grad(vec1, vec2):
    """ Угол между векторами в градусах """
    check_len(vec1, vec2)
    return ((mth.acos(cosine(vec1, vec2))) * 180) / mth.pi


def reversed_vec(vec1, mkcpy=True):
    """ Вектор обратный данному """
    len_is_zero(vec1)
    return vec_scal_prod(vec1, -1, mkcpy)


def collinear(vec1, vec2):
    """ Проверка векторов на коллинеарность векторов """
    check_len(vec1, vec2)
    res = (scalars_are_almost_eq(abs(cosine(vec1, vec2)), 1))
    return res


def parallel(vec1, vec2):
    """ Проверка векторов на сонаправленность """
    check_len(vec1, vec2)
    res = scalars_are_almost_eq(cosine(vec1, vec2), 1)
    return res


def equal(vec1, vec2):
    """ Точное равенство векторов """
    check_len(vec1, vec2)
    res = vec1 == vec2
    return res


def opposite(vec1, vec2):
    """ Проверка векторов на противоположность """
    check_len(vec1, vec2)
    res = scalars_are_almost_eq(cosine(vec1, vec2), -1)
    return res


def ort(vec1, vec2):
    """ ort = orthogonal. Проверка векторов на ортогональность """
    check_len(vec1, vec2)
    res = scalars_are_almost_eq(angle_grad(vec1, vec2), 90)
    return res


def norm(vec1, mkcpy=True):
    """ norm = normalize, find the unit module_vector. Нормировка вектора """
    len_is_zero(vec1)
    result = vector_cpy(vec1, mkcpy)
    for i in range(len(result)):
        result[i] /= mgn(vec1)
    return result


def proj(vec1, vec2):
    """ Численная проекция vec1 на vec2 """
    check_len(vec1, vec2)
    return mgn(vec1) * cosine(vec1, vec2)


def vproj(vec1, vec2, mkcpy=True):
    """ Векторная проекция vec1 на vec2 """
    check_len(vec1, vec2)
    result = vector_cpy(vec2, mkcpy)
    ratio = dot_product(vec1, vec2) / dot_product(vec2, vec2)
    vec_scal_prod(result, ratio, mkcpy=False)
    return result
