primes = []
n = 10000
p = 2
res = [True for i in range(n+1)]
res[0] = res[1] = False
while p*p < n:
    if res[p]:
        for i in range(p*p, n+1, p):
            res[i] = False
    p += 1

for i in range(n+1):
    if res[i]:
        primes.append(i)


def prime_factors(n):
    factors = []

    for i in primes:
        if i < n//2 + 1:
            if n % i == 0:
                factors.append(i)
        else:
            break
    return factors


count = 0

for i in range(12000, 1, -1):
    factors = prime_factors(i)
    for j in range(1, i):
        if j/i > 1/3 and j/i < 1/2:
            for k in factors:
                if j % k == 0:
                    break
            else:
                count += 1

print(count)
