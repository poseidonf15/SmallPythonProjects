import turtle
a = turtle.Pen()
a.speed(0)
a.color("red","red")

a.up()
a.goto(-50,100)
a.right(45)
a.down()

def square():
    for i in range(4):
        a.forward(200)
        a.right(90)

for l in range (10):
    square()
    a.forward(20)
    a.right(15)
