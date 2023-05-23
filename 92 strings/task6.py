string = input("Enter here. : ")
if (len(string) < 3):
    print (string)
elif (string[-3:] == "ing"):
    print (string + "ly")
else :
    print (string + "ing")
