def SingleAddUpNumbers(num):
    value = 0
    for x in range(1, num + 1):
        value += x 
        
    return value


print(SingleAddUpNumbers(600))