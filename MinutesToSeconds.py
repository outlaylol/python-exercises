def MinutesToSeconds(num): 
    min = 0
    for x in range(num):
        min += 60
    return min


print(MinutesToSeconds(2)) 