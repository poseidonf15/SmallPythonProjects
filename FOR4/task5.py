string = input("Enter here. : ")
string2 = ""
num = int(len(string))
for i in range (0,num):
    check = string[i].isalpha()
    if (check):
        string2 = string2 + string[i]
print (string2)
