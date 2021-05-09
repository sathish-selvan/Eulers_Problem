import math

a = 600851475143
def maxPrimneFactor(n):
    while n % 2 == 0:
        max_value = 2
        n /= 1
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            max_value=i
            n = n/i
    if n > 2:
        max_value = n
    return int(max_value)

print(maxPrimneFactor(a))