primes=[]
n = 1000000
p = 2
res = [True for i in range(n+1)]
res[0] = res[1] = False
while p*p < n:
    if res[p]:
        for i in range(p*p,n+1,p):
            res[i] = False
    p += 1
for i in range(n+1):
    if res[i]:
        primes.append(i)
prime_factors = {}
def find_prime(n):
    global prime_factors
    global primes
    ls = []
    for i in primes:
        if i < (n//2)+1:
            if n % i == 0:
                ls.append(i)
    prime_factors[n] = ls
def check_list(n):
    global prime_factors
    if len(prime_factors[n-1]) == len(prime_factors[n-2]) == len(prime_factors[n-3]) == len(prime_factors[n]) == 4:
        return True
    return False
find_prime(99997)
find_prime(99998)
find_prime(99999)
# find_prime(134043)
# find_prime(134044)
# find_prime(134045)
# find_prime(134046)
# print(prime_factors)
# print(check_list(134046))
for i in range(100000,200000):
    print(i)
    find_prime(i)
    if check_list(i):
        print(i)
        break


# problem have to rectify, it takes more time to get result but its working, rework needed