# list1 = [0, 1, 2, 3, 4]

# list1.insert(1, 1)
# list1.remove(1)
# list1.append(5)
# list1.sort()
# list1.pop()
# list1.reverse()

if __name__ == '__main__':
    list1 = []
    N = int(input())
    for _ in range(N):
      user_input = input().split()
      command = user_input[0].lower()
      nums = list(map(int, user_input[1:]))

      if command == "insert":
        list1.insert(nums[0], nums[1])
      elif command == "print":
        print(list1)
      elif command == "remove":
        list1.remove(nums[0])
      elif command == "append":
        list1.append(nums[0])
      elif command == "sort":
        list1.sort()
      elif command == "pop":
        list1.pop()
      elif command == "reverse":
        list1.reverse()