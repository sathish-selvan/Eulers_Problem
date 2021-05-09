import time
start= time.time()
lis = []
for i in range(1,10000):
    a = i ** 3
    b = []
    b[0:] = str(a)
    b.sort()
    lis.append(b)
comparison = []
smallest = 0
for i in lis:
    if i not in comparison:
        comparison.append(i)
for i in comparison:
    count = lis.count(i)
    if count == 5:
        smallest = i
        break
print(lis.index(smallest)+1)
print(time.time()-start,"secs")