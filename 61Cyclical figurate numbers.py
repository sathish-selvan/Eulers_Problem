from itertools import permutations
import time
time_start = time.time()
triangle = []
i = 1
p = 1
while len(str(p)) < 5:
    p = (i * (i+1)) // 2
    if len(str(p)) == 4:
        triangle.append(p) 
    i += 1

square = []
i = 1
p = 1
while len(str(p)) < 5:
    p = i **2
    if len(str(p)) == 4:
        square.append(p)
    i += 1

pentagonal = []
i = 1
p = 1
while len(str(p)) < 5:
    p = (i *(3*i-1)) // 2
    if len(str(p)) == 4:
        pentagonal.append(p)
    i += 1

hexagonal = []
i = 1
p = 1
while len(str(p)) < 5:
    p = (i * (2*i-1)) 
    if len(str(p)) == 4:
        hexagonal.append(p)
    i += 1

heptagonal = []
i = 1
p = 1
while len(str(p)) < 5:
    p = (i * (5*i-3))//2
    if len(str(p)) == 4:
        heptagonal.append(p)
    i += 1


octagonal = []
i = 1
p = 1
while len(str(p)) < 5:
    p = (i * (3*i-2))
    if len(str(p)) == 4:
        octagonal.append(p)
    i += 1

print(triangle)
print(square)
print(pentagonal)
print(hexagonal)
print(heptagonal)
print(octagonal)
luck = False
total = []
total.append(triangle)
total.append(square)
total.append(pentagonal)
total.append(hexagonal)
total.append(heptagonal)
total.append(octagonal)
a = permutations([i for i in range(1,len(total))])
posiible = []
passed = False
for z in a:
    PATH = list(z)
    for i in triangle:
        for j in total[PATH[0]]:
            if str(i)[2:] == str(j)[:2]:
                for k in total[PATH[1]]:
                    if str(j)[2:] == str(k)[:2]:
                        for l in total[PATH[2]]:
                            if str(k)[2:] == str(l)[:2]:
                                for m in total[PATH[3]]:
                                    if str(l)[2:] == str(m)[:2]:
                                        for n in total[PATH[4]]:
                                            if str(m)[2:] == str(n)[:2] and str(n)[2:] == str(i)[:2]:
                                                posiible.append (i)
                                                posiible.append (j)
                                                posiible.append (k)
                                                posiible.append (l)
                                                posiible.append (m)
                                                posiible.append (n)
                                                passed = True
                                                break
                                    if passed:
                                        break
                            if passed:
                                break
                    if passed:
                        break
            if passed:
                break
    if passed:
        break
print(posiible)
print(time.time() - time_start,"secs")