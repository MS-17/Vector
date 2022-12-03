from src.module_vector import vector as vc
from src.module_matrix import matrix as mtr


# Matrices merging. Always makes copy of mtr1 and never changes mtr2
def merge_mtr(mtr1, mtr2):
    """ Слияние двух матриц, всегда делает копию 1-ой матрицы, 2 матрица не изменяется """
    mtr.check_matrix(mtr1)
    mtr.check_matrix(mtr2)

    if not vc.len_is_equal(mtr1, mtr2):
        raise ValueError("There should be equal number of rows in the matrices")

    res = mtr.mtr_cpy(mtr1, True)

    for i, j in zip(res, mtr2):
        i += j

    return res


# Returns matrix that has all 1s on the main diagonal and all 0s under it. Always changes mtr1 inside.
# If logs argument is True, the intermediate results of operations will be printed
def move_forward(mtr1, logs=False):
    """
        На выходе матрица, у которой на главной диагонали все 1, а под главной диагональю - все 0.
        Изменяет mtr1. Если logs=True, то выводит промежуточные результаты преобразований данной матрицы
    """
    mtr_len = len(mtr1)

    for i in range(mtr_len):

        # check if there's 0 in the mtr1[i][i]. If so we should swap this row with a row that doesn't contain 0
        if mtr1[i][i] == 0:
            mtr.swapRows(mtr1, idx1=i, idx2=i + 1, do_copy=False)

        mtr.row_div_scl(mtr1, index=i, scalar=mtr1[i][i], do_copy=False)

        if i == len(mtr1):
            break

        for j in range(i + 1, mtr_len):
            mtr.sum_rows(mtr1, index1=j, index2=i, scalar1=1, scalar2=-mtr1[j][i], do_copy=False)

        if logs:
            print(mtr1)


# mtr1 should be the result of the move_forward operation
# Returns the identity matrix. Always changes mtr1 inside. If logs argument is True
# the intermediate results of operations will be printed
def move_backward(mtr1, logs=False):
    """
        На вход матрица, у которой на главной диагонали все 1,под главной диагональю - все 0.
        На выходе получается единичная матрица. Изменяет mtr1. Если logs=True, то
        выводит промежуточные результаты преобразований данной матрицы
     """
    mtr_len = len(mtr1)

    for i in range(mtr_len - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            mtr.sum_rows(mtr1, index1=j, index2=i, scalar1=1, scalar2=-mtr1[j][i], do_copy=False)

        if logs:
            print(mtr1)


# Performs the Gauss-Jordan matrix elimination. mtr1 argument should be a merged matrix. Always changes mtr1
# if logs == True, the intermediate results of operations will be printed
# This function uses move_forward() and move_backward()
def gauss(mtr1, logs=False):
    """
        Реализация алгоритма Гаусса. На вход необходимо передать уже расширенную матрицу.
        Данная функция изменяет переданную матрицу. Если logs=True, то
        выводит промежуточные результаты преобразований данной матрицы
    """
    # move forward
    move_forward(mtr1, logs)

    # move backward
    move_backward(mtr1, logs)

    return mtr1


# Returns a list (vector) containing the linear system solutions. Never changes mtr1 and mtr2
# if logs == True, the intermediate results of operations will be printed
# This function uses gauss()
def get_solution(mtr1, mtr2, logs=False):
    """
        Получение строки (вектора), содержащей решение уравнения. Не изменяет mtr1 и mtr2.
        Если logs=True, то выводит промежуточные результаты преобразований матрицы mtr1
    """
    res = merge_mtr(mtr1, mtr2)

    gauss(res, logs)

    solution = mtr.getCol(res, len(res[0]) - 1)

    return solution
