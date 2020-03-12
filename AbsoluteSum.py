def AbsoluteSum(arr): 
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]

    return sum


print(AbsoluteSum(list([2, 4, 6, 8, 10])))