# geting a wrong answer

a="None,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen"
ones = list(map(str,a.split(",")))
b ="None,ten,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety"
tens = list(map(str,b.split(",")))
res = ""
for i in range(1, 20):
    res += ones[i]
for i in range(20,99):
    if i % 10 == 0:
        res +=tens[i//10]
    else:
        res +=tens[i//10] + ones[i%10]
for i in range(100,1000):
    if i % 100 == 0:
        res += ones[i//100]+"hundred"
    else:
        sa = i % 100
        res += ones[i//100]+"hundredand"
        if 10 < sa < 20:
            res += ones[sa]
        else:
            if sa % 10 == 0:
                res +=tens[sa//10]
            elif sa < 10:
                res += ones[sa % 10]
            else:
                res += tens[sa//10] + ones[sa%10]
res +="onethousand"
print(res)
print(len(res))



