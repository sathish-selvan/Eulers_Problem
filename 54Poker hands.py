
def player_score(a):
    player1 = a
    PALYER1 = list(map(str,player1.split(" ")))
    print(PALYER1)
    numz = []
    sym = []
    for i in PALYER1:
        numz.append(i[-2::-1][::-1])
        sym.append(i[-1])
    print(numz)
    print(sym)
    ref = ["0",'1','2','3','4','5','6','7','8','9','T','J',"Q","K","A"]
    num = []
    for i in numz:
        num.append(ref.index(i))
    print(num)
    cons = []
    for i in range(1, 11):
        cons.append((list(i for i in range(0+i, 5+i))))
    if set(sym) == set("D") or set(sym) == set("C") or set(sym) == set("H") or set(sym) == set("S"):
        ROYAL_FLUSH = set([10,11,12,13,14])
        if set(num) == ROYAL_FLUSH:
            print( "Royal flush",(10+11+12+13+14)*100000000)
        elif num in cons:
            print("Straight Flush", num)
            sum(num)*10000000
        else:
            print("Flush with "+str(sym[0])+" "+str(sum(num)*100))
            return sum(num)*1000000
    else :
        dum = []
        for i in num:
            if i not in dum:
                dum.append(i)
        pairs = {}
        support = []
        for i in dum:
            support.append(num.count(i))
            pairs[i]=(num.count(i))
        print(pairs)
        if 4 in support:
            a = max(pairs, key=pairs.get)
            print("fours of ",a)
            return a * 100000
        elif 3 in support and 2 in support:
            a = max(pairs, key=pairs.get)
            # b = min(pairs, key=pairs.get)
            print("house full of "+ "three ",a )
            return a * 10000
        elif 3 in support:
            a = max(pairs, key=pairs.get)
            print("three's of " + "3 * ",a)
            return a * 1000
        elif 2 in support:
            a = max(pairs, key=pairs.get)
            print("pair's of ",a)
            return a * 100
        elif num in cons:
            print("Straight ", num)
            return num * 10
        else:
            print("max card ",max(dum))
            return max(dum)

def convert(a):
    player1 = a
    PALYER1 = list(map(str, player1.split(" ")))
    num = a
    print(PALYER1)
    numz = []
    sym = []
    for i in PALYER1:
        numz.append(i[-2::-1][::-1])
        sym.append(i[-1])
    print(numz)
    print(sym)
    ref = ["0", '1', '2', '3', '4', '5', '6','7', '8', '9', 'T', 'J', "Q", "K", "A"]
    num = []
    for i in numz:
        num.append(ref.index(i))
    return num

def check(a):
    if a is None : return None
    num = a
    cons = []
    for i in range(1, 11):
        cons.append((list(i for i in range(0+i, 5+i))))
    dum = []
    for i in num:
        if i not in dum:
            dum.append(i)
    pairs = {}
    support = []
    for i in dum:
        support.append(num.count(i))
        pairs[i] = (num.count(i))
    print(pairs)
    if 4 in support:
        a = max(pairs, key=pairs.get)
        print("fours of ", a)
        return a * 100000
    elif 3 in support and 2 in support:
        a = max(pairs, key=pairs.get)
        # b = min(pairs, key=pairs.get)
        print("house full of " + "three ",a )
        return a * 10000
    elif 3 in support:
        a = max(pairs, key=pairs.get)
        print("three's of " + "3 * ", a)
        return a * 1000
    elif 2 in support:
        a = max(pairs, key=pairs.get)
        print("pair's of ", a)
        return a * 100
    elif num in cons:
        print("Straight ", num)
        return num * 10
    else:
        print("max card ", max(dum))
        return max(dum)


p1 = player_score('4D 6S 9H QH QC')
p2 = player_score("3D 6D 7H QD QS")
if p1>p2:
    print("Player 1")
elif p2 > p1:
    print("Player 2")
if p1 == p2:
    print("hihi")
    p1 = convert('4D 6S 9H QH QC')
    p2 = convert("3D 6D 7H QD QS")
    a =[]
    b=[]
    for i in p1:
        if i not in p2:
            a.append(i)
    for i in p2:
        if i not in p1:
            b.append(i)
    if check(a)>check(b):
        print("Player 1")
    else:
        print("player 2")
