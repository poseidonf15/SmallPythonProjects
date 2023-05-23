import turtle
a = turtle.Pen()
num = 400
a.up()
a.goto(-200,-200)
a.down()
a.width(5)
x = 0
a.speed(9)
while (x < 40):
    a.forward(num)
    a.left(90)
    num = num - 10
    x = x + 1
