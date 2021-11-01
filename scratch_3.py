import math
def sqrt2(n):
    if n==1: return 1.4
    else:
     return math.sqrt(2+sqrt2(n-1))
print(sqrt2(111))
