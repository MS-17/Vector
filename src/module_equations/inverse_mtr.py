import src.module_equations.linear_system as lns
from src.module_matrix.matrix import matrix_mltp
from src.module_vector.vector import len_is_equal


# Get identity matrix with given rows number
def get_identity(rows):
    """ Создает единичную матрицу с заданным кол-вом строк """
    res = []
    res += [[0 for j in range(rows)] for i in range(rows)]
    for i in range(rows):
        res[i][i] = 1
    return res


# Extract inverse matrix from the matrix eliminated by Gauss-Jordan method. mtr1 is not changed
def extract(mtr1):
    """ Получает обратную матрицу из расширенной матрицы, преобразованной методом Гаусса-Жордана. Не меняет mtr1 """

    if len(mtr1[0]) % 2 != 0:
        raise ValueError("The matrix length should be an even number")

    res = []
    for i in mtr1:
        res += [i[int(len(mtr1[0]) / 2):]]
    return res


# Get inverse matrix of the given matrix. mtr1 is not changed
def inverse(mtr1):
    """ Получить обратную матрицу из обычной переданной матрицы. Не меняет mtr1 """

    if not len_is_equal(mtr1, mtr1[0]):
        raise ValueError("The matrix should be square")

    identity = get_identity(len(mtr1))
    res = lns.merge_mtr(mtr1, identity)
    lns.gauss(res)
    res = extract(res)

    return res


# get the linear system solution using inverse matrix method. mtr1 and mtr2 are not changed
def inverse_matrix_method(mtr1, mtr2):
    """
        Получить решение системы уравнений матричным способом. mtr1 - матрица коэффициентов уравнения,
        mtr2 - матрица свободных членов. Не меняет mtr1 и mtr2
    """
    inverse_mtr1 = inverse(mtr1)
    res = matrix_mltp(inverse_mtr1, mtr2)
    return res


a = [[1, 2, 3], [4, 3, 3], [2, -1, 1]]
b = [[1], [-0.3], [8]]
print(inverse_matrix_method(a, b))

