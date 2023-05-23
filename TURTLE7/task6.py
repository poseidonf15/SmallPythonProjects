import turtle
a = turtle.Pen()
a.width(3)

x = 50
for l in range(5):
    for i in range(4):
        a.forward(x)
        a.right(90)
    x += 20
