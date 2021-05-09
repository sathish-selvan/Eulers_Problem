import numpy as np
n = 100
primes = []
res = [True for i in range(n+1)]
p = 2
res[0] = res[1] = False
while p*p < n:
    if res[p]:
        for i in range(p*p,n+1,p):
            res[i] = False
    p += 1

for i in range(n+1):
    if res[i] :
        primes.append(i)
for x in range(11,n):
    amount = x
    money = []
    for i in primes:
        if i < amount:
            money.append(i)
        else:
            break

    a = np.ones((len(money), amount+1))
    for j in range(1, amount+1):
        if j % money[0] == 0:
            a[0][j] = 1
        else:
            a[0][j] = 0
    for i in range(1, len(money)):
        for j in range(1, amount+1):
            if money[i] > j:
                a[i][j] = a[i-1][j]
            else:
                a[i][j] = a[i-1][j]+a[i][j-money[i]]
    if int(a[len(money)-1][amount]) > 5000:
        print(x)
        break
