res = 0
for i in range(1,1001):
    res += i**i
res = str(res)
print(res[-1:-11:-1][::-1])