n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())
for i in range(n_commands):
  command = input().split()
  com_key = command[0]
  if com_key == "pop":
    s.pop()
  elif com_key == "discard":
    s.discard(int(command[1]))
  elif com_key == "remove":
    s.remove(int(command[1]))
print(sum(s))
