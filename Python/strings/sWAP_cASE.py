def swap_case(s):
  new_str = ""
  for letter in s:
    if letter == letter.lower():
        new_let = letter.upper()
        new_str += new_let
    elif letter == letter.upper():
        new_let = letter.lower()
        new_str += new_let
  return 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# there is a .swapcase() in python and honestly fuh this shi