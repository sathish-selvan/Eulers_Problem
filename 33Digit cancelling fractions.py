def div(a,b):
    l1 = []
    l2 = []
    l1[0:] = str(a)
    l2[0:] = str(b)
    for i in l1:
        if i not in l2:
            continue
        else:
            l1.remove(i)
            l2.remove(i)
    x = int(l1[0])
    y = int(l2[0])
    return x/y
    
res = 1
for i in range(12,100):
    for j in range(11,i):
        if str(j)[-1] == str(i)[0]:
            # if not (len(set(str(i))) == 1 and len(set(str(i))) == 1):
            if not (i % 10 == 0 or j % 10 == 0):
                    if j/i == div(j,i):
                        print(f"{j}/{i}")
                        res *= i/j
print(int(res))


