import turtle
import time
a = turtle.Pen()
a.speed(0)
a.hideturtle()

a.left(90)

for i in range(12):
    a.up()
    a.forward(100)
    a.down()
    a.backward(25)
    a.up()
    a.backward(75)
    a.right(30)
    a.down()

for i in range(360):
    a.color("black", "black")
    a.forward(50)
    time.sleep(0.95)
    a.color("white", "white")
    a.backward(50)
    a.right(6)








