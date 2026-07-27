# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

#     getScores = student_marks[query_name]
#     totalScores = 0
    
#     for i in getScores:
#         totalScores += i

#     average = totalScores / len(getScores)
#     print(f"{average:.2f}")


# -------------------------------------------------------
# import numpy as np

# rows, columns = map(int, input().split())
# empty_array = []
# for i in range(rows):
#     my_array = input().split()
#     be_array = list(map(int, my_array))
#     empty_array.append(be_array)

# transposed_array = np.transpose(empty_array)
# print(transposed_array)

# flatten_array = np.array(empty_array)
# be_flattened = flatten_array.flatten()
# print(be_flattened)

# ----------------------------------------------------
# array1 = numpy.array([1,2,3])
# array2 = numpy.array([4,5,6])

# extended_array = numpy.concatenate((array1, array2))

# n, m, p = map(int, input().split())
# n_array = []
# m_array = []
# for _ in range(n):
#   new_array = list(map(int, input().split()))
#   n_array.append(new_array)

# for _ in range(m):
#   new_array = list(map(int, input().split()))
#   m_array.append(new_array)

# joint_array = numpy.concatenate((n_array, m_array), axis=0)
# print(joint_array)
#

# import numpy

# # Read all numbers from the input line
# dims = list(map(int, input().split()))

# # Use the list directly as the shape!
# matrix_zero = numpy.zeros(dims, dtype=int)
# matrix_ones = numpy.ones(dims, dtype=int)

# print(matrix_zero)
# print(matrix_ones)
  
# import numpy
# numpy.set_printoptions(legacy='1.13')

# n, m = map(int, input().split())

# matrix = numpy.eye(n, m)

# print(matrix)

# n, m = map(int, input().split())

# array_a = []
# for _ in range(n):
#   row = list(map(int, input().split()))
#   array_a.append(row)

# array_b = []
# for _ in range(n):
#   row = list(map(int, input().split()))
#   array_b.append(row)

# a = numpy.array(array_a)
# b = numpy.array(array_b)

# print(numpy.add(a, b))
# print(numpy.subtract(a, b))
# print(numpy.multiply(a, b))
# print(numpy.floor_divide(a, b))
# print(numpy.mod(a, b))
# print(numpy.power(a, b))

# numpy.set_printoptions(legacy='1.13')

# input_array = list(map(float, input().split()))

# new_array = numpy.array(input_array)

# print(numpy.floor(new_array))
# print(numpy.ceil(new_array))
# print(numpy.rint(new_array))

# import numpy

# n, m = map(int, input().split())
# empty_array = []

# for _ in range(n):
#   input_array = list(map(int, input().split()))
#   empty_array.append(input_array)

# total_sum = numpy.sum(empty_array, axis=0)

# product = numpy.prod(total_sum)

# print(product)

import numpy

n, m = map(int, input().split())
empty_array = []
for _ in range(n):
  input_array = list(map(int, input().split()))
  empty_array.append(input_array)

total_min = numpy.min(empty_array, axis=1)
maximum = numpy.max(total_min)
print(maximum)