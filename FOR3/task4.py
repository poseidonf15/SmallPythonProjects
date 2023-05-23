num2 = 1
for i in range (6):
    if (i == 0):
        num = int(input("Enter here. : "))
    if (i > 0):
        num2 = int(input("Enter here. : "))
        if (num == 0 and num2 == 0):
            num = 1
        elif (num == 0):
            num2 *= 1
        elif (num2 == 0):
            num *= 1
        else:
            num *= num2
print (num)
