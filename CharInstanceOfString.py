

def CharInstanceOfString(character, string):
    chars = list(string)
    amount = 0
    for x in range(len(chars)):
         if (character == chars[x]): amount+=1

    return amount



print(CharInstanceOfString("b", "big fat bubble"))