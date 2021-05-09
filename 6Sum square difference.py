n = int(input("Enter the value: "))
a = [i for i in range(1,n+1)]
b = sum([i**2 for i in a])
c = sum(a) ** 2
print(c-b)
