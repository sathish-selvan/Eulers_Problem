import math
def seive(n):
    primes=[]
    res = [True for i in range(n+1)]
    p = 2
    while p*p < n:
        if res[p] == True:
            for i in range(p*p,n+1,p):
                res[i] = False
        p += 1
    for i in range(2,n+1):
        if res[i]:
            primes.append(i)
    return primes
global PRIMES
PRIMES = seive(90000)
print("Created the prime list")

def is_prime(x):
    global PRIMES
    if x in PRIMES:
        return True
    else:
        return False

nMax = 0
aMax = 0
bMax = 0
for a in range(1000, -1000,-1):
    for b in range(1000,-1000,-1):
        
        n = 0
        while(is_prime(abs(n*n + n*a + b))):
            n+= 1
        if n > nMax:
            aMax = a
            bMax = b
            nMax = n
            print(nMax,aMax,bMax)
print(aMax*bMax)




