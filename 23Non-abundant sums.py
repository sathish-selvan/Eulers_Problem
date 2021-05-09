limit = 28123
def abundant_number(n):
    res = []
    for i in range(1,(n//2)+1):
        if n % i == 0:
            res.append(i)
    if sum(res) > n:
        return True
    else:
        return False

ran = []
for i in range(1, 28124):
    ran.append(i)
abund= []
for i in range(12,28123):
    if abundant_number(i):
        abund.append(i)
print("task 1")
progress = []
for i in abund:
    for j in abund:
        if i + j < 28123:
            if i+j in ran:
                ran.remove(i+j)
        else:
            break
print(sum(ran))

