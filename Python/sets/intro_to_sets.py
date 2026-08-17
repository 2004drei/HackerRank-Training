def average(array):
  # your code goes here
  arr = set(list(array))
  ave = sum(set(arr))
  return ave / len(arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)