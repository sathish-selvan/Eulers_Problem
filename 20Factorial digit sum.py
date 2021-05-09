def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)
res = str(factorial(100))
result = 0
for i in res:
    result += int(i)
print(result)