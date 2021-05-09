# Algorithm for division

primes = []
n = 1000
dummy = [True for i in range(n+1)]
p = 2

while p*p < n:
    if dummy[p]:
        for i in range(p*p, n+1, p):
            dummy[i] = False
    p += 1

for i in range(2, n+1):
    if dummy[i]:
        primes.append(i)

print(primes)
length = 0
value = 0
a = 0
for i in range(len(primes)):
    CJ = []
    denum = primes[i]
    num = 1000
    output = ''
    remainder = 1
    for _ in range(0, 2000):
        if num < denum:
            output += "0"
            num *= 10
        else:
            quotient = num//denum
            output += str(quotient)
            remainder = num % denum
            if not remainder == 0 and remainder < denum:
                remainder *= 10

            num = remainder
    for j in range(2, 999):

        if output[0:j] == output[j:j*2]:
            a = j
            break

    if a > length:
        length = a
        value = primes[i]

print("Value :", value, "----> Length :", length)
