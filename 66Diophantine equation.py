import math
large = 0
for k in range(2,100):
    gonext = False
    for i in range(2,1000):
        for j in range(1,(i//2)+2):
            if k*(j**2) == (i**2)-1:
                print(f"{i}^2 - {k}*{j}^2 = 1")
                if i > large:
                    large=i
                    value = k
                gonext = True
                break
        if gonext:
            break

print(large)
print(value)