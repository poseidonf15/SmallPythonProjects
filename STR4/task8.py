string = input("Enter two words. : ")
find = string.find(" ")
x = len(string[:find])
x2 = len(string[find + 1:])
if (x < x2):
    print (string[find + 1:] + " " + string[:find])
else:
    print(string)
