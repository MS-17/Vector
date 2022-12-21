import src.module_equations.linear_system as lns


print("\n!!!The functions move_forward(), move_backward() and gauss() change first parameter by default. "
      "However, they allow to make argument copies by using do_copy=True parameter!!!\n")
print("2D linear systems usage:")
a = [[-0.1, -1], [5, 2]]
b = [[3.5], [-2]]
print("a:", a, "\tb:", b)

merge = lns.merge_mtr(a, b)
print("a and b merged:", merge)

mv_frd = lns.move_forward(merge, True)
print("Move_forward, do_copy=True:", mv_frd, "\tmerge matrix:", merge, "\tmv_frd:", mv_frd)

print("Move_backward:",  lns.move_backward(mv_frd), "\tmv_frd matrix:", mv_frd)

merge1 = lns.merge_mtr(a, b)
print("Gauss method:",  lns.gauss(merge1),  "\tmerge1 matrix:", merge1)

solution = lns.get_solution(a, b)
print("Get_solution:",  solution)


print("\n3D linear systems usage:")
c = [[-1, 2.5, 4.22], [3.1, -1.11, 0], [4, 1, 1.5]]
d = [[10.2], [-1], [33]]
print("c:", c, "\td:", d)

merge = lns.merge_mtr(c, d)
print("c and d merged:", merge)

print("Move_forward:", lns.move_forward(merge), "\tmerge matrix:", merge)

print("Move_backward:",  lns.move_backward(merge), "\tmerge matrix:", merge)

merge2 = lns.merge_mtr(c, d)
gs = lns.gauss(merge2, True)
print("Gauss method, do_copy=True:", gs,  "\tmerge2 matrix:", merge2)

solution = lns.get_solution(a, b)
print("Get_solution:",  solution)


print("\nThere shouldn't be only column vector for merging. The only requirement is that matrices have equal"
      " rows number", lns.merge_mtr([[2, 3, -22], [5, 23, 84.4829]], [[100, 200, 500.00001], [21.3, 0.9, 11.222]]))

# this solution works only for the linear systems that have solutions
# what if the linear system has no solutions or many of them?
# what if we got 2 or 3 0s in the column or row?
# there could be all 0 on the diagonal
# there could be more than 1 zero in a row
