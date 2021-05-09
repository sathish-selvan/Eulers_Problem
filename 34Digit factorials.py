
upper = 2540160 #refered from mathblock dk
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def isCurious(n):
    m = n
    a = 0
    while n != 0:
        a += fact(n%10)
        n = n // 10 
    if a == m:
        return True
    else:
        return False

progress = 0
for i in range(3,upper):
    if isCurious(i):
        progress += i
print(progress)

