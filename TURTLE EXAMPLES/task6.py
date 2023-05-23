import turtle
a = turtle.Pen()
a.speed(0)

for i in range (180):
    a.forward(100)
    a.right(15)
    a.forward(25)
    a.left(30)
    a.forward(50)

    a.up()
    a.goto(0,0)
    a.right(17)
    a.down()
