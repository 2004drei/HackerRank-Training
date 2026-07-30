from __future__ import division

a = int(input())
b = int(input())

result_divmod = divmod(a, b)

print(a // b)
print(result_divmod[1])
print(divmod(a, b))