result = 2
a = 1
b = 2
for i in range(2,4000000):
    c = a+b
    a = b
    b = c
    if c % 2 == 0:
        result += c
print(result)

# this is shit