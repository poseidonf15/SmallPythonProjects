import turtle
a = turtle.Pen()
a.speed(0)
a.width(3)

x = (200)
for l in range(5):
    for i in range(4):
        a.forward(x)
        a.right(90)
    a.up()
    a.forward(10)
    a.right(90)
    a.forward(10)
    a.left(90)
    a.down()
    x -= 20
