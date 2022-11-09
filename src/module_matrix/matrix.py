from src.module_vector import vector as vc
from src.module_vector.vector import len_is_equal


def mtr_cpy(mtr1, do_copy=True):
    if do_copy:
        # res = copy.deepcopy(mtr1)
        res = []
        for i in mtr1:
            res += [i * 1]
    else:
        res = mtr1
    return res


# every element is a list (or list like)
def is_fully_nested(mtr1):
    """ True, если все элементы вложенные, представляют список """
    return all(isinstance(i, list) for i in mtr1)


# all elements are not lists (or lists like)
def is_not_nested(mtr1):
    """ True, если нет ни одного вложенного элемента """
    return all(not (isinstance(i, list)) for i in mtr1)


# False if fully nested or not nested at all. Uses is_not_nested() and is_fully_nested()
def incorrectly_nested(mtr1):
    """
        True, если список выглядит следующим образом: [3, [1], 2]. False, если все строки матрицы -
        векторы (списки) или ни один из элементов не является вектором (списком)
    """
    return not is_not_nested(mtr1) and not is_fully_nested(mtr1)


# check if matrix len is 0. Uses len_is_equal() and if_fully_nested()
def null_check(mtr1):
    if len_is_equal(mtr1, []):
        raise ValueError("Matrix should be more than 1 * 1 dimension")
    if is_fully_nested(mtr1):
        for i in mtr1:
            if len_is_equal(i, []):
                raise ValueError("There should be no empty elements in the matrix")


# check if matrix looks like that: [[2], 1]. Uses incorrectly_nested()
def check_if_incorrectly_nested(mtr1):
    if incorrectly_nested(mtr1):
        raise ValueError("The matrix cannot look like the following [[2], 1]. Each element should be nested or "
                         "none of them should be nested at all")


# check if the length of each row is equal. Uses is_fully_nested() and len_is_equal()
def rows_are_equal(mtr1):
    if is_fully_nested(mtr1):
        for i in mtr1:
            if not len_is_equal(i, mtr1[0]):
                raise ValueError("Length of each row should equal in the matrix")


# Uses null_check(), check_if_incorrectly_nested(), rows_are_equal()
def check_matrix(mtr1):
    null_check(mtr1)
    check_if_incorrectly_nested(mtr1)
    rows_are_equal(mtr1)


# def incorrect_row_vector(mtr1):
#     """ Вернет ValueError, если вектор строка выглядит следующим образом: [[1, 2]] """
#     if is_fully_nested(mtr1) and len_is_equal(mtr1, [1]) and not len_is_equal(mtr1[0], [1]):
#         raise ValueError("The row vector shouldn't look that way: [[2, 3]]. "
#                          "If you want to use a single row, pass it like the following: [2, 3]")


# True is row vector. Uses check_matrix() and is_not_nested(), len_is_equal(), is_fully_nested()

def incorrect_row_vector(mtr1):
    """ Вернет ValueError, если вектор строка выглядит следующим образом: [1, 2], или [[1]]"""
    if is_not_nested(mtr1) or len_is_equal(mtr1[0], [1]):
        raise ValueError("The row vector shouldn't look that way: [1, 2]. "
                         "If you want to use a single row, pass it like the following: [[2, 3]]")


# def row_vector(mtr1):
#     """
#         True, если вектор (список) вида [1, 2, 3], а также для списка вида [[1, 2]], но False для [[1]].
#         Для иных случаев - False. Для вектора строки вида [[1, 2]] вернет ValueError
#     """
#     check_matrix(mtr1)
#     incorrect_row_vector(mtr1)
#     return is_not_nested(mtr1) or (is_fully_nested(mtr1) and len_is_equal(mtr1, [1]) and not len_is_equal(mtr1[0], [1]))


def row_vector(mtr1):
    """
        True, если вектор (список) вида [[1, 2, 3]]. Для иных случаев - False. Для вектора строки вида [[1, 2]] вернет ValueError
    """
    incorrect_row_vector(mtr1)
    return True


def column_vector(mtr1):
    """ True, если вектор (список) вида [[1], [2], [3]]. False иначе, в том числе для вектора (списка) вида [1] """
    check_matrix(mtr1)
    return is_fully_nested(mtr1) and all(
        len(i) == 1 for i in mtr1)  # or (is_not_nested(mtr1) and len_is_equal(mtr1, [1]))


# this check is used for addition and subtraction
def check_dimension(mtr1, mtr2):
    check_matrix(mtr1)
    check_matrix(mtr2)

    incorrect_row_vector(mtr1)
    incorrect_row_vector(mtr2)

    if not len_is_equal(mtr1, mtr2):
        raise ValueError("The rows number should equal")

    if (row_vector(mtr1) and column_vector(mtr2)) or (row_vector(mtr2) and column_vector(mtr1)):
        raise ValueError("Cannot add (subtract) vector row and vector column")

    if is_fully_nested(mtr1) and is_fully_nested(mtr2):
        for i, j in zip(mtr1, mtr2):
            if not len_is_equal(i, j):
                raise ValueError("The rows length should equal")


def check_mtr_mltp(mtr1, mtr2):
    if (row_vector(mtr1) and row_vector(mtr2)) or (row_vector(mtr1) and not len_is_equal(mtr1, mtr2) and
                                                   is_fully_nested(mtr2)) or \
            (is_fully_nested(mtr1) and not len_is_equal(mtr1[0], mtr2)):
        raise ValueError("The matrix1 columns number should equal the matrix2 rows number")


'''
def matrix_sum(mtr1, mtr2, do_copy=True):
    check_dimension(mtr1, mtr2)
    res = mtr_cpy(mtr1, do_copy)
    for i in range(len(res)):
        res[i] = [j + k for j, k in zip(res[i], mtr2[i])]
    return res


def matrix_diff(mtr1, mtr2, do_copy=True):
    check_dimension(mtr1, mtr2)
    res = mtr_cpy(mtr1, do_copy)
    for i in range(len(res)):
        res[i] = [j - k for j, k in zip(res[i], mtr2[i])]
    return res


def scalar_mlt(mtr1, scalar, do_copy=True):
    null_check(mtr1)
    res = mtr_cpy(mtr1, do_copy)
    for i in range(len(res)):
        # res[i] = 
    return res

'''


# use vectors
def matrix_sum(mtr1, mtr2, do_copy=True):
    check_dimension(mtr1, mtr2)
    res = mtr_cpy(mtr1, do_copy)
    for i in range(len(res)):
        vc.vsum(res[i], mtr2[i], mkcpy=False)
    return res


def matrix_diff(mtr1, mtr2, do_copy=True):
    check_dimension(mtr1, mtr2)
    res = mtr_cpy(mtr1, do_copy)
    for i in range(len(res)):
        vc.vdiff(res[i], mtr2[i], mkcpy=False)
    return res


def matrixT(mtr1, do_copy=True):
    check_matrix(mtr1)
    res = []
    rows = len(mtr1)
    cols = len(mtr1[0])
    temp = []
    for i in range(cols):
        for j in range(rows):
            temp += [mtr1[j][i]]
        res += [temp]
        temp = []

    if do_copy:
        return res

    mtr1.clear()
    mtr1 += res
    return mtr1


def matrix_mltp(mtr1, mtr2, do_copy=True):
    check_mtr_mltp(mtr1, mtr2)  # there's no need to use check_matrix() here because matrices are both
    # already checked in check_mtr()

    res = []

    # for i in mtr1

    if do_copy:
        return res

    mtr1.clear()
    mtr1 += res
    return mtr1


# a = [1, 2, 2]
# b = [2, 2, 9]
# print("Initial matrices:\t", "a:", a, "\t", "b:", b, end="\n\n")
# print("Sum:", matrix_sum(a, b), "\ta:", a)
# print("Diff:", matrix_diff(a, b), "\ta:", a)
# print("Transpose:", matrixT(a), "\ta:", a)

print(row_vector([[1], [2]]))

# print(check_mtr_mltp([3, 2], [[1], [2]]))
# print("Checkers:")
# print(check_matrix([[1], [2]]))
# print(row_vector([[1, 2], [1, 2]]))
# print(column_vector([[1, 2], [1, 2]]))
# print(check_dimension([[1]], [[1]]))
# print(incorrectly_nested([1, 2, 3]))
# print(is_not_nested([[1], [2]]))
# print(is_fully_nested([1, 2]))
