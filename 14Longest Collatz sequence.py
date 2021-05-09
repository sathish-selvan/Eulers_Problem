dic = {n: 0 for n in range(1, 1000000)}
dic[1] = 1
dic[2] = 2
for i in range(3, 1000000):
    counter = 0
    num = i
    while i > 1:
        if i < num:
            dic[num] = dic[i] + counter
            break
        if i % 2 == 0:
            i = i/2
            counter += 1
        else:
            i = 3*i + 1
            counter += 1
print(max(dic, key=dic.get))
