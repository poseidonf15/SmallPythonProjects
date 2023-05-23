string = input("Enter here. : ")
if (len(string) > 10):
    print (string[:9] + string[10:])
elif (len(string) == 10):
    print (string[:9])
else:
    print (string)


    
