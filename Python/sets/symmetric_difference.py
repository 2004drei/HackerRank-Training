m = int(input())
m_set = set(list(map(int, input().split())))

n = int(input())
n_set = set(list(map(int, input().split())))

m_diff = sorted(m_set.difference(n_set))
n_diff = sorted(n_set.difference(m_set))

combined = m_diff + n_diff
combined.sort()
for i in combined:
  print(i)