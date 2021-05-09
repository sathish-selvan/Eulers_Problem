import math
no_of_factors = 0
a = 1
while not no_of_factors > 500:
    no_of_factors = 0
    
    b = int((a*(a+1))/2)
    counter = 0
    for i in range(1,int(math.sqrt(b)+1)):
        if b % i == 0:
            counter += 1
            if i is not b/i:
                counter += 1
    no_of_factors = counter 
    a += 1
print(b)


