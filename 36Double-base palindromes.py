def isPal(s):
    if s == s[::-1]:
        return True
    else:
        return False
res = 0
for i in range(10,999999):
    if isPal(str(i)) and isPal(bin(i)[2:]):
        res += i
        print(i)
print(res)
