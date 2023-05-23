string = input("Enter a line : ")
x = string.find("a")
x2 = string.find("A")
y = string.find("b")
y2 = string.find("B")

if (x == -1):
    x3 = x2
elif (x2 == -1) :
    x3 = x
else :
    if (x <= x2):
        x3 = x
    elif (x2 < x):
        x3 = x2

if (y == -1):
    y3 = y2
elif (y2 == -1) :
    y3 = y
else :
    if (y <= y2):
        y3 = y
    elif (y2 < y):
        y3 = y2

if (x == -1 and x2 == -1 and y == -1 and y2 == -1):
    print ("Error")
elif (x3 < y3):
    print ("""The letter "a" was first.""")
else:
    print ("""The letter "b" was first.""")
