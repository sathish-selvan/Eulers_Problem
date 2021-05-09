from itertools import permutations

n = 8000000
res = [True for i in range(n+1)]
p = 2

while p*p < n:
    if res[p]:
        for i in range(p*p,n+1,p):
            res[i] = False
    p += 1
primes=[]
for i in range(2,n+1):
    if res[i]:
        primes.append(i)

print(primes[-1])
s = "123456789"
res = 0
for i in  range(2,9):
    com = s[:i]
    a = permutations(com)
    for i in a:
        pan = int("".join(i))
        if pan in primes:
            if res < pan:
                res = pan
                print(res)
print(res)


