import turtle
a = turtle.Pen()

def triangle():
    a.forward(50)
    a.right(120)
    a.forward(50)
    a.left(120)

def triangle2():
    a.forward(100)
    a.right(120)
    a.forward(100)
    a.left(120)

a.up()
a.goto(-350,-50)
a.down()

a.color("sienna","sienna")
a.begin_fill()

a.left(90)
a.forward(50)
a.right(30)

num = 0

while (num < 3):
    num = num + 1
    triangle()

num = 0

while (num < 4):
    num = num + 1
    triangle2()

num = 0

while (num < 3):
    num = num + 1
    triangle()
    
a.right(150)
a.forward(50)
a.end_fill()





























    






