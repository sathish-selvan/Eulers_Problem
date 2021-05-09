from itertools import permutations
from itertools import combinations

a =permutations([1,2,3,4,5,6,7,8,9,10][::-1],3)
lisa = []
for i in a:

    b = list(map(int,i))
    if sum(b) == 14:
        lisa.append(b)

bal = combinations(lisa,5)
for i in bal:
    baloon = list(i)
    if baloon[0][0] + baloon[1][0] + baloon[2][0] + baloon[3][0] + baloon[4][0] == 10+9+8+7+6:
        if baloon[0][2] == baloon[1][1] and baloon[1][2] == baloon[2][1] and baloon[2][2] == baloon[3][1] and baloon[3][2] == baloon[4][1] and baloon[4][2] == baloon[0][1]:
            check_list = baloon[0][1:] + baloon[1][1:] + baloon[2][1:] + baloon[3][1:] + baloon[4][1:]
            if baloon[0][0] not in check_list and baloon[1][0] not in check_list and baloon[2][0] not in check_list and baloon[3][0] not in check_list and baloon[4][0] not in check_list:
                final = baloon

chumma = [final[0][0] , final[1][0] ,final[2][0] ,final[3][0] ,final[4][0] ]
store = chumma.index(min(chumma))
print(store)
res = [final[store]]+final[0:store]
string = ''
for i in res:
    for j in i:
        string += str(j)

print(string)