n = 3
max_limit = (10 ** n) -1
min_limit = 1 + max_limit // 10
largest_num = 0
for i in range(max_limit,min_limit,-1):
    for j in range(i,min_limit,-1):
        mul = i * j
        if mul < largest_num:
            break
        reverse = str(mul)[::-1]
        if mul == int(reverse):
            largest_num = mul
print(largest_num)

# this one also works XD
number = 0
for i in range(100, 1000):
    for j in range(100, i):
        a = i * j
        if str(a) == str(a)[::-1]:
            if a > number:
                number = a

print(number)
