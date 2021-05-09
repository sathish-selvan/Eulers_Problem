def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
value = 0
for i in range(23,101):
    for j in range(i):
        if  fact(i)//(fact(j)* fact(i-j)) > 1000000:
            value = value + 1
print(value)

