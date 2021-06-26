
def palindrome_check(word1, word2):
    #tried .reverse at end and it kept returning None
    pal1 = list(word1)
    pal2 = list(word1)
    print(word1,word2,pal1,pal2)
    if word1 == pal1 and word2 == pal2:
        return True
    else:
        return False

print(palindrome_check("rotor", "rotor"))
