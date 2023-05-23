string = input("Enter here. : ")
i = 0
num = 0
numx = ""
num2 =  0
num2x = ""

while (i < len(string) - 1):
    b = i
    if (i < 2):
        if (string[b].isalpha()):
            while (string[b].isalpha()):
                num += 1
                numx = numx + string[b]
                i += 1
                b = i
    while (string[b].isalpha()):
        num2 += 1
        num2x = num2x + string[b]
        i += 1
        b = i
    if (string[b].isalpha()):
        print("")
    elif (num2 > num):
        num = num2
        numx = num2x
        num2 = 0
        num2x = ""
    i += 1
    b = i
print (numx)
                









