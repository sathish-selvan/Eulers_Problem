primes = []
n = 1000
p = 2
res = [True for i in range(n+1)]
res[0] = res[1] = False
while p*p < n:
    if res[p]:
        for i in range(p*p, n+1, p):
            res[i] = False
    p += 1

for i in range(2, n+1):
    if res[i]:
        primes.append(i)
print(primes)


def prime_factors(n):
    global primes
    factors = []
    for i in primes:
        if i < n:
            if n % i == 0:
                factors.append(i)
    return factors

max_values = []

for i in range(3, n):
    near_primes = []
    a = prime_factors(i)
    b = [True for j in range(i)]
    b[0] = False
    for k in a:
        for j in range(k, i, k):
            b[j] = False
    for z in range(i):
        if b[z]:
            near_primes.append(z)
    max_values.append(i / len(near_primes))

print(max_values.index(max(max_values))+3)

# aletnative efficient methodology

primes = []
n = 100
p = 2
res = [True for i in range(n+1)]
res[0] = res[1] = False
while p*p < n:
    if res[p]:
        for i in range(p*p, n+1, p):
            res[i] = False
    p += 1

for i in range(2, n+1):
    if res[i]:
        primes.append(i)
print(primes)

a = int(input("Enter the max value range : ")) # Enter your max value here
Max = 1
for i in primes:
    if Max * i > a:
        print(Max)
        break
    Max *= i


