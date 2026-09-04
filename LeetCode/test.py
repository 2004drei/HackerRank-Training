def fizzBuzz(n):
  """
  :type n: int
  :rtype: List[str]
  """
  emptyList = []
  for i in range(1, n+1):
    emptyList.append(str(i))
  for i in emptyList:
    indexu = emptyList.index(i)
    if int(i) % 3 == 0 and int(i) % 5 == 0:
      emptyList[indexu] = "FizzBuzz"
    elif int(i) % 3 == 0:
      emptyList[indexu] = "Fizz"
    elif int(i) % 5 == 0:
      emptyList[indexu] = "Buzz"

  return emptyList

n = 3
print(fizzBuzz(n))