
n, m = list(map(int, input().split()))
n_array = list(map(int, input().split()))
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

happiness = 0
for i in n_array:
  if i in A and i not in B:
    happiness += 1
  elif i in B:
    happiness -= 1
print(happiness)