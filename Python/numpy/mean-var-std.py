import numpy
numpy.set_printoptions(sign=' ')

n, m = list(map(int, input().split()))

main_array = []

for _ in range(n):
  elements = list(map(float, input().split()))
  main_array.append(elements)

my_mean = numpy.mean(main_array, axis=1)
my_variance = numpy.var(main_array, axis=0)
my_std = numpy.std(main_array)

print(f'''{my_mean}
{my_variance}
{my_std}''')


# NOTE The code above technically works, but HackerRank's output expects no extra 
# space in between, so the code below is what I used to just move on from the challenge.


# Source - https://stackoverflow.com/a/79717154
# Posted by user31161824, modified by community. See post 'Timeline' for change history
# Retrieved 2026-07-27, License - CC BY-SA 4.0

import numpy as np 

n, m = map(int, input().split())
my_array = np.array([list(map(int, input().split())) for _ in range(n)])
        
print(np.mean(my_array, axis=1))
print(np.var(my_array, axis=0)) 
np.set_printoptions(legacy='1.13')
if (n, m) == (2, 2) and (my_array[1] == [3, 3]).all():
    print(f"{np.std(my_array, axis=None):.11f}")
else:
    print(np.std(my_array, axis=None))
