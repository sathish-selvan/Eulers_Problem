# https: // en.wikipedia.org/wiki/Pentagonal_number
# i got the formul from above mentioned wikipedia website
import math

def isPenta(n):
    m = (math.sqrt(24*n + 1)+1)/6
    if m == int(m):
        return True
    else:
        return False
i = 2
result = 0
found = True
while found:
    m = i*(3*i - 1)//2
    for j in range(i,0,-1):
        n = j*(3*j - 1)//2
        
        if isPenta(m+n) and  isPenta(m-n):
            result = m-n
            found = False
            break
    i+=1
print(result)

