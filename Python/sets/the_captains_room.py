K = int(input())
elements_list = list(map(int, input().split()))
elements_set = set(elements_list)

for i in list(elements_set):
  elements_list.remove(i)

cap_rnum = elements_set.difference(set(elements_list)).pop()

print(cap_rnum)


