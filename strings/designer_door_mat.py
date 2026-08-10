N, M = list(map(int, input().split()))

for i in range(N//2):
  pattern = (".|."*(2*i+1) ).center(M,"-")
  print(pattern)

print("WELCOME".center(M, "-"))

for i in range(N//2 - 1, -1, -1):
  r_pattern = (".|."*(2*i+1)).center(M,"-")
  print(r_pattern)