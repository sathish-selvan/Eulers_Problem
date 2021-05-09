
s = ""
counter = 1
while len(s) < 1000000:
    s += str(counter)
    counter+= 1

res = 1
for i in range(0,7):
    res *= int(s[1 * (10**i)])
print(res)
