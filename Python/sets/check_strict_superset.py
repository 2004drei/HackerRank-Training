A= set(map(int, input().split()))
n = int(input())
is_True = 0
is_False = 0
for i in range(n):
  n_set = set(map(int, input().split()))
  if A.issuperset(n_set):
    is_True += 1
  else:
    is_False +=1

if is_False != 0:
  print('False')
else:
  print('True')