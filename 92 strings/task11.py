string = input("Enter here. : ")
num = len(string)
x = 1
i = 0
num = num // 2

while (i < num):
    if (i == 0):
        string2 = string[x]
    if (i > 0):
        string2 = string2 + string[x]
    i += 1
    x += 2
print (string2)
