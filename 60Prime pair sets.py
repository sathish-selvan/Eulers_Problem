import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    else:
        return True
primes = []
n = 1000000
res = [True for i in range(n+1)]
p = 2
while p*p < n:
    if res[p]:
        for i in range(p*p,n+1,p):
            res[i] = False
    p += 1
for i in range(2,n+1):
    if res[i]:
        primes.append(i)
print(len(primes))
fin =[]
luck = False
for i in range(0,10):
    print(i)
    a =primes[i]
    checker = []
    for j in range(i+1,2000):
        b =primes[j]
        if is_prime(int(str(a)+str(b))) and is_prime(int(str(b)+str(a))):
            for k in range(j+1,2000):
                c = primes[k]
                if is_prime(int(str(a)+str(c))) and is_prime(int(str(c)+str(a))) and is_prime(int(str(b)+str(c))) and is_prime(int(str(c)+str(b))):
                    for l in range(k+1, 2000):
                        d = primes[l]
                        if is_prime(int(str(a)+str(d))) and is_prime(int(str(d)+str(a))) and is_prime(int(str(b)+str(d))) and is_prime(int(str(d)+str(b))) and is_prime(int(str(c)+str(d))) and is_prime(int(str(d)+str(c))):
                            for m in range(k+1, 2000):
                                e = primes[m]
                                if is_prime(int(str(a)+str(e))) and is_prime(int(str(e)+str(a))) and is_prime(int(str(b)+str(e))) and is_prime(int(str(e)+str(b))) and is_prime(int(str(c)+str(e))) and is_prime(int(str(e)+str(c))) and is_prime(int(str(d)+str(e))) and is_prime(int(str(e)+str(d))):
                                    checker.append(a)
                                    checker.append(b)
                                    checker.append(c)
                                    checker.append(d)
                                    checker.append(e)
                                    luck = True
                                    break
                                if luck:
                                    break
                            if luck:
                                break
                        if luck:
                            break
                    if luck:
                        break
                if luck:
                    break
            if luck:
                break
        if luck:
            break
    if luck:
        break
print(sum(checker[0:5]))

# its working but takes about 1 minute to get answer, its sad but my code workss hehe
