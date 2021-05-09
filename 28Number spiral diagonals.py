number = 1001 * 1001

diagonals = []

n = 1
counter = 2
while n < number:
    for _ in range(0,4):
        n += counter
        diagonals.append(n)
    counter += 2
dia1 = 0
dia2 = 0
for i in range(0,len(diagonals)):
    if i % 2 == 0:
        dia1 += diagonals[i]
    else:
        dia2 += diagonals[i]
print(dia1+dia2+n)
