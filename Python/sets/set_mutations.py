n = int(input())
A = set(map(int, input().split()))
n_of_sets = int(input())

for _ in range(n_of_sets):
  command = input().split()
  N = set(map(int, input().split()))
  com_key = command[0]
  if com_key == "intersection_update":
    A.intersection_update(N)
  elif com_key == "update":
    A.update(N)
  elif com_key == "symmetric_difference_update":
    A.symmetric_difference_update(N)
  elif com_key == "difference_update":
    A.difference_update(N)

print(sum(A))

