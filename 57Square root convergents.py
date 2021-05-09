import math
a = 0
n = 1
d = 1
for i in range(1,1000):
    n,d = 2*d + n, d+n
    if int(math.log10(n)) > int(math.log10(d)):
        a += 1
print(a)

