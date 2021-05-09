triangle= []

with open("C:/Users/Sathis/Desktop/my codes/ilink internship/Programming Task/67.txt") as f:
    for i in range(0,100):
        a = f.readline()
        b = list(map(int,a.split()))
        triangle.append(b)



res = triangle[0][0]
index = 0
for i in range(1,100):
    a = index -1
    b = index +1
    c = index
    if a != abs(a):
        if triangle[i][b] > triangle[i][c] :
            res += triangle[i][b]
            index = b
        else:
            res += triangle[i][c]
            index = c
    elif b > i+1:
        if triangle[i][a] > triangle[i][c]:
            res += triangle[i][a]
            index = a
        else:
            res += triangle[i][c]
            index = c
    else:
        if triangle[i][a] > triangle[i][b] and triangle[i][a] > triangle[i][c]:
            res += triangle[i][a]
            index = a

        elif triangle[i][b] > triangle[i][c]:
            res += triangle[i][b]
            index = b
        
        else:
            res += triangle[i][c]
            index = c
    
    print(triangle[i])
    print(index)
    
print(res)
