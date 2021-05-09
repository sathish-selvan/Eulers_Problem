import math
# lic = {}
# for i in range(10,1000):
#     pub = set()
#     for a in range(1,i//3):
#         for b in range(1,i//2):
#             for c in range(1,i//2):
#                 if a+b+c == i:
#                         if c ** 2 ==a ** 2 + b ** 2:
#                             lol = [a,b,c]
#                             lol.sort()
                            
#                             pub.add(tuple(lol))
                            
#     lic[i] = len(pub)
#     print(i,len(pub),pub)
# print(max(lic, key=lic.get))

# effici

l1 = [0 for i in range(1001)]
print(l1[120])
for a in range(1, 500):
    for b in range(1, 500):
        c = math.sqrt(a**2 + b**2)
        if int(c) == c and a < b and b < c and a+b+c <= 1000:
            l1[int(c+a+b)] += 1
print(l1)
print(l1.index(max(l1)))
for i in range(0,len(l1)):
    if l1[i] == 2:
        print(i)