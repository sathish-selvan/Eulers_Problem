current = 0
fraction = ""
for i in range(10000,1,-1):
    for j in range(1,i):
        if j/i < 3/7:
            if j/i > current:
                current = j/i
                a = str(j)+"/" + str(i)
                fraction = a

print(fraction)
