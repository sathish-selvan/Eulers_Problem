from itertools import permutations
def chreah(n):
    dad = []
    s = str(n)
    for _ in range(len(s)):
        g = s[1:]+s[0]
        s = g
        dad.append(s)
    return dad

def seive():
    n = 1000000
    primes=[]
    res = [True for _ in range(n+1)]
    p = 2
    while p*p < n:
        if res[p]:
            for j in range(p*p,n+1,p):
                res[j] = False
        p += 1
    for i in range(2,n+1):
        if res[i]:
            primes.append(i)
    print("pimes list created")
    circularprimes=[]
    for i in primes:
        flag = False
        a = chreah(i)
        for j in a:
            b = "".join(list(j))
            if int(b) in primes:
                continue
            else:
                flag = True
                break
        if not flag :
            circularprimes.append(i)
            print(i)
    print(len(circularprimes))
seive()






