string = input("Enter the password : ")
x1 = string.isalnum()
x2 = string.isalpha()
if (x1 == True and x2 == False):
    print ("True")
else :
    print ("False")
