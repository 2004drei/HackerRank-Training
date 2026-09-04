import itertools

S, I = input().split()

sortedu = sorted(list(itertools.permutations(S, int(I))))

for i in sortedu:
  per = ''
  for x in i:
    per += x
  print(per)  

