import numpy
numpy.set_printoptions(legacy='1.13')

x = int(input())
determinant = [list(map(float, input().split())) for _ in range(x)]

print(numpy.linalg.det(determinant))