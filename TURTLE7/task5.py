import turtle
a = turtle.Pen()
a.width(3)
a.speed(0)

def Rectangle():
    for x in range(2):
        for i in range(3):
            for l in range(2):
                a.forward(80)
                a.left(90)
                a.forward(60)
                a.left(90)
            a.up()
            a.forward(100)
            a.down()
        if (x == 0):
            a.up()
            a.backward(300)
            a.right(90)
            a.forward(80)
            a.left(90)
            a.down()
            
    a.up()
    a.backward(300)
    a.right(90)
    a.forward(20)
    a.left(90)
    a.forward(100)
    a.down()
    for l in range(4):
        for i in range(4):
            a.forward(80)
            a.right(90)
        a.up()
        a.right(90)
        a.forward(100)
        a.left(90)
        a.down()

    a.up()
    a.goto(-165,-250)
    a.down()
    
    for i in range(4):
        a.forward(50)
        a.right(90)
    a.up()
    a.forward(70)
    a.down()
    
    for i in range(4):
        a.forward(30)
        a.right(90)
    a.up()
    a.forward(50)
    a.down()

    for i in range(4):
        a.forward(90)
        a.right(90)
    a.up()
    a.forward(110)
    a.down()

    for i in range(4):
        a.forward(10)
        a.right(90)
    a.up()
    a.forward(30)
    a.down()

    for i in range(4):
        a.forward(40)
        a.right(90)
    a.up()
    a.forward(60)
    a.down()


a.up()
a.goto(-150,250)
a.down()
Rectangle()


