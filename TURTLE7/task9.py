import turtle
a = turtle.Pen()
a.width(3)
a.speed(0)

a.up()
a.backward(100)
a.down()

for i in range(3):
    a.forward(50)
    a.right(90)
for i in range(2):
    a.backward(50)
    a.left(90)

a.up()
a.left(90)
a.forward(20)
a.down()

for i in range(2):
    a.forward(50)
    a.left(90)
    a.forward(100)
    a.left(90)

a.up()
a.forward(70)
a.left(90)
a.forward(100)
a.right(90)
a.down()

for i in range(3):
    a.forward(50)
    a.right(90)
for i in range(2):
    a.backward(50)
    a.left(90)

a.up()
a.left(90)
a.forward(20)
a.down()

a.left(90)
a.forward(100)

