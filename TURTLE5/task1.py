import turtle
t = turtle.Pen()
t.width(3)

for i in range (5):
    t.forward(150)
    t.left(360/5)

t.up()
t.right(90)
t.forward(100)
t.down()

for i in range (10):
    t.forward(50)
    t.left(360/10)

t.up()
t.right(90)
t.forward(200)
t.left(90)
t.down()

for i in range (12):
    t.forward(50)
    t.left(360/12)

