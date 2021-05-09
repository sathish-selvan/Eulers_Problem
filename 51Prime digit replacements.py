primes = []
n = 999999
p = 2
res = [True for i in range(n+1)]
while p*p < n:
    if res[p]:
        for i in range(p*p, n+1, p):
            res[i] = False
    p += 1
for i in range(2, n+1):
    if res[i]:
        primes.append(i)
sec = []
for j in range(100000, n+1):
    if res[j]:
        sec.append(j)
found = False
print(res[120383])
for i in sec:
    a = "0"+str(i)
    b = []
    b[0:] = a
    num = list(map(str, [i for i in range(0, 10)]))
    for j in range(1, len(a)):
        for k in range(j+1, len(a)):
            for l in range(k+1, len(a)):
                simple = []
                count = 0
                for z in range(0, 10):
                    if z == 0:
                        check = 4
                    else:
                        check = int("".join(b[:j])+num[z]+"".join(b[j+1:k])+num[z]+"".join(b[k+1:l])+num[z]+"".join(b[l+1:]))
                    if res[check]:
                        simple.append(check)
                        count += 1
                if count == 8:
                    print(simple[0])
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break
