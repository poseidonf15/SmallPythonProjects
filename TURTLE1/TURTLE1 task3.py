n = int(input("Enter how many fance do you want? : "))
import turtle
a = turtle.Pen()
a.up()
a.goto(-200,-100)
a.down()
a.width(3)
a.color("black","grey")
i = 0
while (i < n):
    a.left(90)
    a.begin_fill()
    a.forward(200)
    a.right(45)
    a.forward(25)
    a.right(90)
    a.forward(25)
    a.right(45)
    a.forward(200)
    a.left(90)
    a.end_fill()
    i = i + 1
    
    
