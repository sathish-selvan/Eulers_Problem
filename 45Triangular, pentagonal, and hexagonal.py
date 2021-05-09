# unknown formula
import math
def isPenta(n):
    m = (math.sqrt(24*n+1)+1)/6
    if m == int(m):
        return True
    else:
        return False

i = 144
while True:
    hex = i*(2* i - 1)
    if isPenta(hex):
        print(hex)
        break
    i += 1

