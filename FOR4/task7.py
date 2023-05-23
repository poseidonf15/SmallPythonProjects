string = input("Enter here. : ")
num = len(string)
word = ""

for i in range (0,num):
    if (string[i].isalpha()):
        word = word + string[i]
        if (string[i + 1].isalpha()):
            print ("")
        else:
            break
print (word)
        

    
