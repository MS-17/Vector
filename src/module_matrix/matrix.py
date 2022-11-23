from src.module_vector import vector as vc
from src.module_vector.vector import len_is_equal


# if do_copy = True, copies the passed matrix, else returns the matrix itself
def mtr_cpy(mtr1, do_copy=True):
    """Если do_copy = True, возвращает копию переданной матрицы, иначе возвращает ту же матрицу"""
    if do_copy:
        res = []
        for i in mtr1:
            res += [i * 1]
    else:
        res = mtr1
    return res


# every element is a list (or list like)
def is_fully_nested(mtr1):
    """ True, если все элементы вложенные, т е представляют список """
    return all(isinstance(i, list) for i in mtr1)


# all elements are not lists (or lists like)
def is_not_nested(mtr1):
    """ True, если нет ни одного вложенного элемента - списка """
    return all(not (isinstance(i, list)) for i in mtr1)


# False if the list is fully nested or not nested at all. Uses is_not_nested() and is_fully_nested()
def incorrectly_nested(mtr1):
    """
        True, если список выглядит следующим образом: [3, [1], 2] или ни один элемент не является list.
        False, если все строки матрицы - векторы (списки)
    """
    return not (is_not_nested(mtr1) or is_fully_nested(mtr1)) or is_not_nested(mtr1)


# check if matrix looks like that: [[2], 1]. Uses incorrectly_nested()
def check_if_incorrectly_nested(mtr1):
    if incorrectly_nested(mtr1):
        raise ValueError("The matrix cannot look like the following [[2], 1]. Each element should be nested or "
                         "none of them should be nested at all.\nIf you want a vector row pass it like the following: "
                         "[[1, 2, 3]]")


# check if the matrix len is 0. Uses len_is_equal() from src.module_vector.vector
def null_check(mtr1):
    """ Проверяет есть ли хоть один пустая строка в матрице """
    if len_is_equal(mtr1, []):
        raise ValueError("Matrix should be more than 1 * 1 dimension")

    for i in mtr1:
        if len_is_equal(i, []):
            raise ValueError("There should be no empty elements in the matrix")


# check if the length of each row is equal. Uses len_is_equal()
def rows_are_equal(mtr1):
    for i in mtr1:
        if not len_is_equal(i, mtr1[0]):
            raise ValueError("Length of each row should equal in the matrix")


# Uses null_check(), check_if_incorrectly_nested(), rows_are_equal() from src.module_vector.vector
def check_matrix(mtr1):
    """ Проверяет корректность введенной матрицы"""
    check_if_incorrectly_nested(mtr1)
    null_check(mtr1)
    rows_are_equal(mtr1)


# check if you can add(subtract) 2 matrices
def check_dimension(mtr1, mtr2):
    """ Проверяет на возможность сложения(вычитания) 2 матриц """
    if not len_is_equal(mtr1, mtr2):
        raise ValueError("The rows number should equal")

    for i, j in zip(mtr1, mtr2):
        if not len_is_equal(i, j):
            raise ValueError("The rows length should equal")


# check if you can multiply 2 matrices
def check_mtr_mltp(mtr1, mtr2):
    """ Проверяет на возможность умножения 2 матриц """
    if not len_is_equal(mtr1[0], mtr2):
        raise ValueError("There should equal number of columns in the first matrix and rows in the second one")


# check if 2 matrices are almost equal, uses vec_are_almost_equal() from src.module_vector.vector
def mtr_are_almost_equal(mtr1, mtr2):
    """Проверяет 2 матрицы на равенство с учетом возможной ошибки числа с плавающей точкой"""
    return all(vc.vec_are_almost_eq(i, j) for i, j in zip(mtr1, mtr2))


# sum matrices
def matrix_sum(mtr1, mtr2, do_copy=True):
    """Сумма матриц"""
    check_matrix(mtr1)
    check_matrix(mtr2)
    check_dimension(mtr1, mtr2)

    res = mtr_cpy(mtr1, do_copy)
    for i in range(len(res)):
        vc.vsum(res[i], mtr2[i], mkcpy=False)
    return res


# subtract matrices
def matrix_diff(mtr1, mtr2, do_copy=True):
    """Разность матриц"""
    check_matrix(mtr1)
    check_matrix(mtr2)
    check_dimension(mtr1, mtr2)

    res = mtr_cpy(mtr1, do_copy)
    for i in range(len(res)):
        vc.vdiff(res[i], mtr2[i], mkcpy=False)
    return res


# transpose matrix
def matrixT(mtr1, do_copy=True):
    """Транспонирование матрицы"""
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


# multiply a matrix by a scalar
def matrix_scalar_mlt(mtr1, scalar, do_copy=True):
    """Умножение матрицы на скаляр"""
    check_matrix(mtr1)

    res = mtr_cpy(mtr1, do_copy)

    return [vc.vec_scal_prod(i, scalar, mkcpy=False) for i in res]


# divide a matrix by a scalar
def matrix_scalar_div(mtr1, scalar, do_copy=True):
    """Деление матрицы на скаляр"""
    check_matrix(mtr1)

    res = mtr_cpy(mtr1, do_copy)

    return [vc.vec_scal_div(i, scalar, mkcpy=False) for i in res]


# the matrix multiplication
def matrix_mltp(mtr1, mtr2, do_copy=True):
    """Умножение матриц"""
    check_matrix(mtr1)
    check_matrix(mtr2)
    check_mtr_mltp(mtr1, mtr2)

    res = []
    temp = matrixT(mtr2)

    for i in mtr1:
        row = []
        for j in temp:
            row += [vc.dot_product(i, j)]
        res += [row]

    if do_copy:
        return res

    mtr1.clear()
    mtr1 += res
    return mtr1


# get a specified row by index
def getRow(mtr1, index):
    """Получение строки по индексу"""
    check_matrix(mtr1)
    return mtr1[index]


# get a specified column by index
def getCol(mtr1, index):
    """Получение столбца по индексу"""
    check_matrix(mtr1)
    return matrixT(mtr1)[index]


# swap 2 rows
def swapRows(mtr1, idx1, idx2, do_copy=True):
    """Меняет 2 строки местами"""
    if idx1 == idx2:
        raise ValueError("Cannot swap a row with itself")

    check_matrix(mtr1)

    res = mtr_cpy(mtr1, do_copy)

    res[idx1], res[idx2] = res[idx2], res[idx1]

    return res


# multiply a specified row(index required) by a scalar
def row_times_scl(mtr1, index, scalar, do_copy=True):
    """Умножение строки по индексу на скаляр"""
    check_matrix(mtr1)
    res = mtr_cpy(mtr1, do_copy)
    res[index] = vc.vec_scal_prod(getRow(res, index), scalar, mkcpy=False)
    return res


# divide a specified row(index required) by a scalar
def row_div_scl(mtr1, index, scalar, do_copy=True):
    """Деление строки по индексу на скаляр"""
    return row_times_scl(mtr1, index, 1 / scalar, do_copy)


# sum(subtract) 2 rows in matrix. Each row can be multiplied by a scalar
# pass 1 / scalar if you want to divide a row by this scalar
# inx_scalar should be a list of [idx1, idx2, scalar1, scalar2]
# idx1 is the index of the first row, idx2 is the index of the second row, scalar1 is a number, which the first row
# will be multiplied by, scalar2 is a number, which the second row will be multiplied by.
# The result of the operation will be written in the row with idx1
def sum_rows(mtr1, *inx_scalar, do_copy=True):
    """
        Сложение(вычитание) строк в матрице. Каждая строка может быть домножена на число. Чтобы разделить строку на
        число можно передать в качестве 1 / scalar.
        Аргумент inx_scalar должен быть списком и содержать следующее элементы: индекс 1 строки, индекс 2 строки,
        число, на которое необходимо умножить 1 строку, число, на которое необходимо умножить 2 строку.
        Результат сложения (вычитания) будет записан в строку по индексу, который был передан 1-ым арументом в inx_scalar
    """
    check_matrix(mtr1)
    res = mtr_cpy(mtr1, do_copy)

    row1 = vc.vec_scal_prod(getRow(mtr1, inx_scalar[0]), inx_scalar[2])
    row2 = vc.vec_scal_prod(getRow(mtr1, inx_scalar[1]), inx_scalar[3])
    res[inx_scalar[0]] = vc.vsum(row1, row2, mkcpy=False)

    return res

