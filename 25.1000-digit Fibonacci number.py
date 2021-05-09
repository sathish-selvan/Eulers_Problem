a = 1
b = 1
flag = True
counter = 2
while flag:
    c = a+b
    counter += 1
    a = b
    b = c
    if c > 10 ** 999:
        print(counter)
        flag = False
