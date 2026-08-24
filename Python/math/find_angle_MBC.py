import math


AB = int(input())
BC = int(input())
AC = math.sqrt((AB^2)+(BC^2))
ratio = AB / BC
radians = math.atan(ratio)
angle = round(math.degrees(radians))

print(f"{angle}\u00b0")