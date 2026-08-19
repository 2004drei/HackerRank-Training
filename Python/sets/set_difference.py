n = int(input())
n_nums = set(map(int, input().split()))
b = int(input())
b_nums = set(map(int, input().split()))

print(len(n_nums.difference(b_nums)))