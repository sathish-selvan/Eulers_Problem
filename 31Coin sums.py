#refered from youtube dynamic programing
import numpy as np
money = [1,2,5,10,20,50,100,200]
amount = 200
a = np.ones((len(money),amount+1))
for j in range(1,amount+1):
    if j % money[0] == 0:
        a[0][j] = 1
    else:
        a[0][j] = 0
for i in range(1,len(money)):
    for j in range(1,amount+1):
        if money[i] > j:
            a[i][j] = a[i-1][j]
        else:
            a[i][j] = a[i-1][j]+a[i][j-money[i]]
print(int(a[len(money)-1][amount]))