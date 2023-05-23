string = input("Enter here. : ")
for symbol in string:
    if (symbol.isdigit()):
        print(2,end = "")
    elif (symbol.isalpha()):
        print(1,end = "")
    else:
        print(3,end = "")
