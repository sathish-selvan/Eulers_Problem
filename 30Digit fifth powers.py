upper = 355000 # refered the upper limit from math blockdk

def power(n):
    a = 0
    
    while n != 0:
        b = n%10
        a += b ** 5 
        n = n//10
    return a

result = 0
for i in range(2,upper):
    if i == power(i):
        result += i
print(result)
