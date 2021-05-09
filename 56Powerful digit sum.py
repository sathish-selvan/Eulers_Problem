res = 1
summing=[]
for i in range(1,100):
    for j in range(0,100):
        a = i ** j
        b = []
        b[0:] =  str(a)
        su = 0
        for k in b:
            su += int(k)
        summing.append(su)
print(max(summing))
