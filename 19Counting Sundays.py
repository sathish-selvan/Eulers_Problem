
#refered from placement season aptitude

months = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
day = ["sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
count = 0
for i in range(1901, 2001):
    if 1900 <= i <= 1999:
        year = 0
    elif 2000 <= i <= 2099:
        year = 5
    a = int(str(i)[2:])
    print(a)
    for j in range(0, 12):
        cal = a + (a//4)+1+months[j]+year
        print(day[cal%7])
        if cal % 7 == 0:
            count += 1
print(count)
