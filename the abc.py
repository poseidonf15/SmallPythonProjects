import turtle
a = turtle.Pen()
a.width(3)
a.speed(0)

def A(x):
    a.left(75)
    a.forward(x)
    a.right(150)
    a.forward(x)
    a.backward(x/2)
    a.left(75)
    a.backward(x/4)
    a.forward(x/4)
    a.right(75)
    a.forward(x/2)
    a.left(75)

def B(x):
    a.forward(x*0.35)
    a.left(45)
    a.forward(x/4)
    a.left(45)
    a.forward(x/6)
    a.left(45)
    a.forward(x/4)
    a.left(45)
    a.forward(x*0.35)
    a.right(90)
    a.backward(x/2)
    a.forward(x)
    a.right(90)
    a.forward(x*0.35)
    a.right(45)
    a.forward(x/4)
    a.right(45)
    a.forward(x/6)
    a.right(45)
    a.forward(x/4)

    a.up()
    a.left(45)
    a.forward(x/2)
    a.left(90)
    a.forward(x*0.20)
    a.down()
    
B(100)
