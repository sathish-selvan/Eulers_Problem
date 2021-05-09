from itertools import permutations
a = permutations("0123456789")
res = 0
for i in a:
    
    num = "".join(i)
    if num[0] != "0":
        if int(num[1:4]) % 2 == 0 and int(num[2:5]) % 3 == 0 and int(num[3:6]) % 5 == 0 and int(num[4:7]) %7 == 0 and int(num[5:8]) % 11 == 0 and int(num[6:9]) % 13 == 0 and int(num[7:10]) % 17 == 0:
            res += int(num)
print(res)
