import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    else:
        return True
# primes = []
# n = 100000000
# res = [True for i in range(n+1)]
# p = 2
# res[0] = res[1] = False
# while p*p < n:
#     if res[p]:
#         for i in range(p*p, n+1,p):
#             res[i] = False
#     p += 1

count = 1
a = 1
counter = 2
diagonals = [1]
while count/(2*counter+1) > 0.10:
    for j in range(0,4):
        a += counter
        if a < 100000000:
            if isPrime(a):
                count += 1
        else:
            if isPrime(a):
                count += 1
    print(count/(2*counter+1),count)
    counter += 2
print(counter-1)
print(count)
