string = input("Enter here. : ")
while (True):
    string2 = string
    string = input("Enter here. : ")
    if (string2[-1] == string[0]):
        print("",end="")
    else:
        print (string2)
        break
    
    
