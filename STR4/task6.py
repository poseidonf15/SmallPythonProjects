string = input("Enter : ")
num = len(string)
i = 0
x = 0
x2 = -1
num2 = 0

if (num % 2 == 1):
    while (i < num):
        if (string[x] == string[x2]):
            num2 += 1
        x += 1
        x2 -= 1
        i += 1
else:
    print("Your line is not a polindrom")

if (num == num2):
    print("Your line is a polindrom")
else:
    print("Your line is not a polindrom")

