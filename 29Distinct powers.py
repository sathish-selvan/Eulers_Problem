power=set()
for a in range(2,101):
    for b in range(2,101):
        power.add(a ** b)
print(len(power))

