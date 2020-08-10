# How do you check if two strings are anagrams of each other ?

def exists( targetCharacter, arr ):
    for currentCharacter in arr:
        if targetCharacter == currentCharacter:
            return True
    return False

def isAnagram( word1, word2):
    lookup = []
    for character in word1:
        lookup.append(character)

    for otherCharacter in word2:
        if exists(otherCharacter,lookup) == False:
            return False

    return True


# print( isAnagram("cat", "act"))       # True
# print( isAnagram("tom", "bob"))       # False
# print( isAnagram("listen", "silent")) # True
print( isAnagram("aa", "a"))  # False