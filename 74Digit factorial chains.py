factorial_list = []

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

for i in range(10):
    factorial_list.append(factorial(i))

def integer_to_list(n):
    return list(map(int,str(n).strip()))

total_mumbers = 0
for values in range(11,1000000):
    checking = 0
    conversion_list = integer_to_list(values)
    count_chain = 1
    list_of_chain = []
    while values !=checking:
        
        for digit in conversion_list:
            checking += factorial_list[digit]
        
        conversion_list = integer_to_list(checking)
        if checking not in list_of_chain:
            
            list_of_chain.append(checking)
            checking = 0
            count_chain += 1
            
        else:
            break
        if count_chain > 61:
            break
    if count_chain == 60:
        total_mumbers += 1


print(total_mumbers)
