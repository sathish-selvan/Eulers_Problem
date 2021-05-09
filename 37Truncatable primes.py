def trunk(n):
    res = set()
    res.add(n)
    a = n
    while n != 0:
        b = n//10
        res.add(b)
        n = b
    for i in range(len(str(a)), 0, -1):
        c = a % (10**i)
        res.add(c)
        a = c
    res.remove(0)
    return res
def seive():
    n = 1000000
    primes = []
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
    print("primes created")
    result = 0
    for i in primes:
        if i > 10:
            a = list(trunk(i))
            for j in a:
                flag = False
                if j in primes:
                    continue
                else:
                    flag = True
                    break
            if not flag:
                print(i)
                result += i
    print(sum(result))

seive()

