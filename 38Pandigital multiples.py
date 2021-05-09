
for i in range(1,99999):
    s = ""
    for j in range(1,6):
        s += str(i*j) 
        if len(s) == 9 and set(s) == set("123456789"):
            print(s)
