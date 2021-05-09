
primes = []
n = 100000
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



def prime_factors(n):
    global primes
    factors = []
    for i in primes:
        
        if n % i == 0:
            factors.append(i)
        if i > n//2 + 1:
            break
    return factors


max_values = []
min_value = 10
num = 0
for i in range(10,100000):
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
    n = len(near_primes)
    
    c = []
    c[0:] = str(i)
    d = []
    d[0:] = str(n)
    c.sort()
    d.sort()
    if c == d:
        print(i,n, i/n)
        if i/n < min_value:
            min_value = i/n
            num = i
    # max_values.append(i / len(near_primes))


# print(max_values.index(min(max_values))+3)

print(min_value, num)


