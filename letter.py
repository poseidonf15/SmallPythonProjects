import turtle
letter = input("Enter a capital letter : ")
color = input("Enter the color : ")
a = turtle.Pen()
a.width(10)
if (letter == "A"):
    a.pencolor(color)
    a.left(65)
    a.forward(100)
    a.right(125)
    a.forward(100)
    a.backward(50)
    a.left(60)
    a.backward(50)
