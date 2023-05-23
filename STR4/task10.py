string = input("Enter the shoping list. : ")
count = string.count(",")
find = -1
find2 = string.find(",")
i = -1

while (i < count):
    if (i != count - 1):
        print (string[find + 1 : find2])
    elif (i == count - 1):
        print (string[find + 1 :])
    find = find2
    find2 = string.find(",",find + 1,)
    i += 1
