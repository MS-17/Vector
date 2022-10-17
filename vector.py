import math as mth


def len_is_zero(vec1):
    """ Проверяет равна ли длина вектора 0 """
    if len(vec1) == 0:
        raise ValueError("The vector length should not be equal to 0")


def check_len(vec1, vec2):
    """
    Проверяет равны ли длины данных векторов 0. Если да
    возвращает ValueError, если нет, то проверяет длины векторов на равенство
    """
    len_is_zero(vec1)
    len_is_zero(vec2)
    if len(vec1) != len(vec2):
        raise ValueError("The lengths of the vectors are not equal!")


def do_copy(vec1, copy=True):
    """ copy=True -> сделать копию vec1, иначе -> вернуть vec1 """
    if copy:
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


def vsum(vec1, vec2, copy=True):
    """ Сумма векторов """
    check_len(vec1, vec2)
    result = do_copy(vec1, copy)
    for i in range(len(result)):
        result[i] += vec2[i]
    return result


def vdiff(vec1, vec2, copy=True):
    """ Разность векторов """
    check_len(vec1, vec2)
    result = do_copy(vec1, copy)
    for i in range(len(result)):
        result[i] -= vec2[i]
    return result


def vec_scal_prod(vec1, scalar, copy=True):
    """ Умножение вектора на число """
    result = do_copy(vec1, copy)
    for i in range(len(result)):
        result[i] *= scalar
    return result


def vec_scal_div(vec1, scalar, copy=True):
    """ Деление вектора на число """
    len_is_zero(vec1)
    if scalar == 0:
        raise ValueError("The scalar shouldn't be equal to 0!")
    return vec_scal_prod(vec1, 1 / scalar, copy)


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


def reversed_vec(vec1, copy=True):
    """ Вектор обратный данному """
    len_is_zero(vec1)
    return vec_scal_prod(vec1, -1, copy)


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


def norm(vec1, copy=True):
    """ norm = normalize, find the unit vector. Нормировка вектора """
    len_is_zero(vec1)
    result = do_copy(vec1, copy)
    for i in range(len(result)):
        result[i] /= mgn(vec1)
    return result


def proj(vec1, vec2):
    """ Численная проекция vec1 на vec2 """
    check_len(vec1, vec2)
    return mgn(vec1) * cosine(vec1, vec2)


def vproj(vec1, vec2, copy=True):
    """ Векторная проекция vec1 на vec2 """
    check_len(vec1, vec2)
    result = do_copy(vec2, copy)
    ratio = dot_product(vec1, vec2) / dot_product(vec2, vec2)
    vec_scal_prod(result, ratio, copy=False)
    return result


# Usage

a, b = [1, 2], [4, 3]

print("Sum:", vsum(a, b), "\ta:", a)
print("Difference:", vdiff(a, b), "\ta:", a)
print("Vec * 5:", vec_scal_prod(a, 5), "\ta:", a)
print("Vec / 5:", vec_scal_div(a, 5), "\ta:", a)
print("Magnitude:", mgn(a))
print("Dot product:", dot_product(a, b))
print("Cosine:", cosine(a, b))
print("Angle between vectors (rad):", angle_rad(a, b))
print("Angle between vectors (grad):", angle_grad(a, b))
print("Reversed vector:", reversed_vec(a), "\ta:", a)
print("Collinear?:", collinear(a, b))
print("Parallel?:", parallel(a, b))
print("Equal?:", equal(a, b))
print("Opposite?: ", opposite(a, b))
print("Orthogonal?:", ort(a, b))
print("Normalize vector:", norm(a), "\ta:", a)
print("Scalar projection:", proj(a, b))
print("Vector projection:", vproj(a, b), "\ta:", a)
print("Check if the vectors are almost equal with an eps precision = 1E-10:", vec_are_almost_eq(a, b))
print("Initial vectors after all those operations:", "\ta:", a, "\tb:", b)

print("Let ex1 = 6 and ex2 = 6.000000000000001")
ex1 = 6
ex2 = 6.000000000000001
print("Does ex1 equal to ex2 with eps precision = 1E-10?", scalars_are_almost_eq(ex1, ex2))




