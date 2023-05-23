string = input("Enter here. : ")
count = string.count(" ")
i = 0
find = 0 
find2 = 0
findX = string.rfind(" ")
findX2 = string.rfind(" ",0,findX - 1)

while (i < count + 1):
    find = find2
    find2 = string.find(" ",find2 + 1,)
    word2 = string[find + 1:find2]
    
    if (i == 0):
        word = string[find + 1:find2]
        
    if (i > 0 and i + 2 < count):
        if (len(word2) > len(word)):
            word = word2
        else:
            word = word
            
    if (i + 2 == count):
        word2 = string[findX2 + 1:findX]
        if (len(word2) > len(word)):
            word = word2
        else:
            word = word
            
    if (i + 1 == count):
        word2 = string[findX + 1:]
        if (len(word2) > len(word)):
            word = word2
        else:
            word = word
        
    i += 1
print (word)
print (len(word))
        
    
