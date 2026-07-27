import numpy

poly_val = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(poly_val, x))