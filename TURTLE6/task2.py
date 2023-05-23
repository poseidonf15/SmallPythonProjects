import turtle

a = turtle.Pen()

a.speed(0)

a.up()
a.goto(-150,-150)
a.down()

def square(x,pen,fill):
    a.color(pen,fill)
    a.begin_fill()
    for i in range(4):
        a.forward(x)
        a.left(90)
    a.end_fill()
    a.forward(x)

for l in range (10):
    for k in range (5):
        if (l % 2 == 1):
            square(30,"black","white")
            square(30,"black","black")
        else:
            square(30,"black","black")
            square(30,"black","white")
    a.backward(300)
    a.left(90)
    a.forward(30)
    a.right(90)
