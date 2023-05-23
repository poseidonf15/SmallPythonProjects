import turtle
a = turtle.Pen()
a.width(5)
a.speed(0)

for l in range(3):
    for i in range(5):
        a.forward(1)
        a.up()
        a.forward(20)
        a.down()

    a.up()
    a.backward(20)
    a.right(90)
    a.forward(20)
    a.right(90)
    a.down()

    for i in range(5):
        a.forward(1)
        a.up()
        a.forward(20)
        a.down()

    a.up()
    a.backward(20)
    a.left(90)
    a.forward(20)
    a.left(90)
    a.down()
