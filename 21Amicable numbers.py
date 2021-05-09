def proper_divisors(n):
    
    survey = []
    for i in range(1,(n//2)+1):
        if n % i == 0:
            survey.append(i)
    value = sum(survey)

    result = []
    for i in range(1, (value//2)+1):
        if value % i == 0:
            result.append(i)
    res = sum(result)
    if res == n and n != value:
        print(n,value)
        return n
    else:
        return 0
# print(proper_divisors(220))
result = 0
for i in range(2,10000):
    a = proper_divisors(i)
    result += a
print(result)
