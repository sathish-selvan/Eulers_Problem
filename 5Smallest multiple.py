# import math
n = int(input("Enter the value : "))
a = [i for i in range(1,n+1)]
# lcm = a[0]
# for i in range(1,len(a)):
#     lcm = lcm*a[i] // math.gcd(lcm,a[i])

# print(lcm)

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm 

x = a[0]
for i in range(1,n):
    func = lcm(x,a[i])
    x = func
print(x)