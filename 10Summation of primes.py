def prime_Number():
    n = 2000000
    prime = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p,n+1,p):
                prime[i] = False
        p += 1
    result = 0
    for i in range(2,n+1):
        if prime[i]:
            result += i
    return result
print(prime_Number())
