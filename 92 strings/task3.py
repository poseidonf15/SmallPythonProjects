string = input("Enter here. : ")
num = len(string)
if (num == 1):
    print ("Empty string")
else:
    print (string[0:2] + string[-2:])
