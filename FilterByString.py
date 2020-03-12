arr = [1,2,3,4,"hello", "asd", "test"]
def FilterByString(arr):
        if(isinstance(arr, str)): return True
        else: return False


filteredByString = filter(FilterByString, arr)
newarr = list()
for element in filteredByString: 
    newarr.append(element)


print(newarr)