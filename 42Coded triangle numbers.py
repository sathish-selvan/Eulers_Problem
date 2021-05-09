# Needed coded file => word.txt

triangleValue = []
for i in range(1,300):
    triangleValue.append((i*(i+1)//2))


with open("C:/Users/Sathis/Desktop/my codes/ilink internship/Programming Task/Coded Triangle.txt") as f:
    a = f.readline()
    b = a.replace('"','')
    names = list(map(str,b.split(",")))

alphabetsLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = [i for i in range(1,27)]

alphabet = list(map(str,alphabetsLetters.strip()))
count = 0
for word in names:
    res = 0
    for letter in word:
        code = alphabet.index(letter)
        number = values[code]
        res += number
    if res in triangleValue:
        print("Triangle")
        count += 1
    else:
        print("Not an Triangle")
print(count)