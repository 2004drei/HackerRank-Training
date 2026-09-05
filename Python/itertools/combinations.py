import itertools

S, k = input().split()

# emptyList= []
# for i in sorted(S):
#   print(i)
#   emptyList.append(i)

# for i in list(itertools.combinations(sorted(emptyList), int(k))):
#   print(i)

for r in range(1, int(k) + 1):
  for i in list(itertools.combinations(sorted(list(S)), r)):
    combi = ''
    for e in list(i):
      combi+=e
    print(combi)



# print(*itertools.combinations(S, int(k)))