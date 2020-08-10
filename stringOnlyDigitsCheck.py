# How do you check if a string contains only digits?

def onlyDigits( string ):

    # for every character in the string
    for i in range(len(string)):
        character = string[i]
        ascii = ord(character)
        #print(ascii)

        if ascii < 48 or ascii > 57:
            return False

    return True


print( onlyDigits("12a4") ) # False
print( onlyDigits("1234") ) # True