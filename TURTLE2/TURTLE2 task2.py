length = int(input("Enter the length of the rectangle : "))
width = int(input("Enter the width of the rectangle : "))
fillcolor = input("Enter the fill color : ")
pencolor = input("Enter the pen color : ")
import turtle
a = turtle.Pen()
a.width(5)
a.color(pencolor,fillcolor)
a.begin_fill()
a.left(90)
a.forward(length)
a.right(90)
a.forward(width)
a.right(90)
a.forward(length)
a.right(90)
a.forward(width)
a.right(90)
a.end_fill()














