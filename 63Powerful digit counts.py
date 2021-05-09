# This problem can be solved by only using the mathematical approach   
# i tired with for loops no currect result

# reference
# https://www.mathblog.dk/project-euler-63-n-digit-nth-power/
import math

result = 0
lower = 0
n = 1

while lower < 10:
    lower = math.ceil(math.pow(10,(n-1)/n))
    result += 10 - lower
    n += 1

print(result)  


# now i change my approach, i solved using loops and its working LOL

count = 0
for i in range(1, 30):
    for j in range(1, 10):
        if i == len(str(j**i)):
            count += 1
print(count)
