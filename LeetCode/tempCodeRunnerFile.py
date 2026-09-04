  for i in emptyList:
    if int(i) % 3 == 0 and int(i) % 5 == 0:
      emptyList[int(i)] = "FizzBuzz"
    elif int(i) % 3 == 0:
      emptyList[int(i)] = "Fizz"
    elif int(i) % 5 == 0:
      emptyList[int(i)] = "Buzz"