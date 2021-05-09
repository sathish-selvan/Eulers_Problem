from itertools import permutations
found = False

primes = []
n = 10000
p =2
rs = [True for i in range(n+1)]

while p*p < n:
    if rs[p] :
        for i in range(p*p,n+1,p):
            rs[i] = False
    p += 1

for i in range(2,n+1):
    if rs[i] :
        primes.append(i)

print("primes created")

for i in range(1488,10000):
    print(i)
    if i in primes:
        check = []
        a = permutations(str(i))
        for z in a:
            s = (int("".join(z)))
            if s not in check and s >= i:
                check.append(s)
        check.sort()
        b = check[0]
        for j in range(1,len(check)):
            d = check[j]
            if d in primes:
                c =  check[j] - b
                d = check[j]
                for k in range(j,len(check)):
                    if check[k] in primes:
                        e = check[k] - d
                        if e <= c:
                            if e == c:
                                print(str(b)+str(check[j])+str(check[k]))
                                found = True
                                break
                        else:
                            break
            if found:
                break
        if found:
            break



