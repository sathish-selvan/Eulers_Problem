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
cons = []
rs = 0
for i in primes:
    rs += i
    if rs < 1000000:
        cons.append(rs)
print(cons)
loly = []
for i in range(0,len(cons)//2):
    for j in range(i+1,len(cons)):
        if cons[j]-cons[i] > 0:
            loly.append(cons[j]-cons[i])
        else:
            break
print(loly)
loly.sort()
for i in loly[::-1]:
    if i in primes:
        print(i)
        break


