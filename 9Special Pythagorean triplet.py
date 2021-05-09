for a in range(1000):
    for b in range(a,1000):
        c = 1000 - a - b
        cond = a < b and b < c
        if c*c == (a*a +b*b) and cond :
            print(a,b,c)