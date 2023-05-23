string = input("Enter here. : ")
num = len(string)
string2 = ""
for i in range (0,num):
    x = string.count(string[i])
    if (x == 1):
        string2 = string2 + string[i]
print (string2)
