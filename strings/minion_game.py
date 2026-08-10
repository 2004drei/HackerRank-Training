def minion_game(string):
  # your code goes here
  stuart = 0
  kevin = 0
  strlen = len(string)

  for i in range(strlen):
    if string[i] in "AEIOU":
      kevin += strlen - i

  stuart = int(strlen*(strlen+1)/2) - kevin

  if stuart > kevin:
    print("Stuart " + str(stuart))
  if kevin > stuart:
    print("Kevin " + str(kevin))
  if kevin == stuart:
    print("Draw")

  return 0

if __name__ == '__main__':
  s = input()
  minion_game(s)