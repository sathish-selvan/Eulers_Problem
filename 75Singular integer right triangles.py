import math

limit = 10000

survey = [0 for i in range(limit)]

zoom = []
for i in range(1,limit//2):
    for j in range(1,i):
        c = math.sqrt(i**2+j**2)
        if int(c) == c and i+j+c < limit:
            survey[int(c+i+j)] += 1

for i in range(limit):
    if survey[i] == 3:
        print(i)