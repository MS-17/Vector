from src.module_vector import vector as vc

a, b = [1, 2], [4, 3]

print("Sum:", vc.vsum(a, b), "\ta:", a)
print("Difference:", vc.vdiff(a, b), "\ta:", a)
print("Vec * 5:", vc.vec_scal_prod(a, 5), "\ta:", a)
print("Vec / 5:", vc.vec_scal_div(a, 5), "\ta:", a)
print("Magnitude:", vc.mgn(a))
print("Dot product:", vc.dot_product(a, b))
print("Cosine:", vc.cosine(a, b))
print("Angle between vectors (rad):", vc.angle_rad(a, b))
print("Angle between vectors (grad):", vc.angle_grad(a, b))
print("Reversed module_vector:", vc.reversed_vec(a), "\ta:", a)
print("Collinear?:", vc.collinear(a, b))
print("Parallel?:", vc.parallel(a, b))
print("Equal?:", vc.equal(a, b))
print("Opposite?: ", vc.opposite(a, b))
print("Orthogonal?:", vc.ort(a, b))
print("Normalize module_vector:", vc.norm(a), "\ta:", a)
print("Scalar projection:", vc.proj(a, b))
print("Vector projection:", vc.vproj(a, b), "\ta:", a)
print("Check if the vectors are almost equal with an eps precision = 1E-10:", vc.vec_are_almost_eq(a, b))
print("Initial vectors after all those operations:", "\ta:", a, "\tb:", b)

print("Let ex1 = 6 and ex2 = 6.000000000000001")
ex1 = 6
ex2 = 6.000000000000001
print("Does ex1 equal to ex2 with eps precision = 1E-10?", vc.scalars_are_almost_eq(ex1, ex2))
