check = "not"
while (check != "OK"):
    first = input("Enter the password: ")
    second = input("verify your password: ")

    if ("123" in first):
        print ("Simple!")

    elif (first != second):
        print ("Different")

    else:
        check = "OK"

print ("OK")
