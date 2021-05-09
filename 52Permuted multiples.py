for i in range(123456,987654):
    a = set(str(i))
    b = str(i*2)
    c = str(i*3)
    d = str(i*4)
    e = str(i*5)
    f = str(i*6)
    if len(str(i)) == len(b) == len(c) == len(d) == len(e) == len(f):
        if set(b) == a and set(c) == a and set(d) == a and set(e) == a and set(f) == a:
            print(i)
            break
