def seive():
    primes =[]
    com=[]
    n = 6000
    rs = [True for i in range(n+1)]
    p =2
    while p*p < n:
        if rs[p]:
            for i in range(p*p, n+1, p):
                rs[i] = False
        p += 1
    for i in range(2,n+1):
        if rs[i]:
            primes.append(i)
        else:
            com.append(i)
    print("primes and com are created")
    oddcoms = []
    for i in com:
        if i%2 != 0:
            oddcoms.append(i)
    print("odd coms done")
    for i in oddcoms:
        accept = False
        for j in primes:
            for k in range(i):
                if i >= j + 2*(k**2):
                    if i == j + 2*(k**2):
                        accept = True
                        break
                else:
                    break
        if accept:
            continue
        else:
            print(i)
            break

seive()

