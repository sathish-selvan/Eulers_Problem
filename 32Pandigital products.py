products = set()
for i in range(999):
    for j in range(9999999):
        s = str(i) + str(j)+ str(i*j)
        if len(s) == 9 and set(s) == set("123456789"):
            products.add(i*j)
            print(i*j)
        elif len(s) > 9:
            break
print(sum(products))
