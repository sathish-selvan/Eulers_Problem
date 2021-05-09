# SieveOfEratosthenes100
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/
primes=[]
def prime_numbers():
    n = 1000005
    prime = [True for i in range(n+1)]
    prime[1] = False
    p = 2
    while p*p <=  n:
        if prime[p] == True:
            for i in range(p*p,n+1,p):
                prime[i] = False
        p += 1
    for i in range(2,n+1):
        if prime[i]:
            primes.append(i)

prime_numbers()
a = 10001
print(primes[a-1])
