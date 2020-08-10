# How do you print duplicate characters from a string?

# key   = names
# value = age
#d = {"Thomas": 24, "Johnavon": 16, "vedant":15, "phoenix": 13}
#print( d["Thomas"])
#print( d.get("vedant"))

def findDups(string):
    d = {}
    output = ""
    for i in range(len(string)):
        currentCharacter = string[i]
        # looking up the currentCharacter to see if it exists in our dictionary
        if currentCharacter not in d:
            d[currentCharacter] = 1
        else:
            output += currentCharacter
            d[currentCharacter] += 1
    return output


print( findDups("abca"))   # a
print( findDups("abcdef")) #    (nothing should print)
print( findDups("xyzyy"))  # yy
print( findDups("abbcadb")) # bab

#
# def findDups( string ):
#
#     output = ""
#     # go through the entire string character by character
#     for i in range(0, len(string)):
#         # search all the forward elements until the end of the string
#         for j in range( i+1, len(string)):
#             # if you see a duplicate character
#             if string[i] == string[j]:
#                 # add that character to the output string (save it )
#                 output += string[i]
#                 # stop early
#                 break
#
#     return output
#
#
# print( findDups("abca")) # a

