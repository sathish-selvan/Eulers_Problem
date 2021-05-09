nonLy = []
def isLycherl(n):
    global nonLy
    dum = []
    for _ in range(0, 50):
        n = n+int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            nonLy += dum
            return False
        dum.append(n)
    else:
        return True

count = 0
for i in range(10, 10000):
    print(i)
    if i not in nonLy:
        if isLycherl(i):
            count += 1
print(count)
