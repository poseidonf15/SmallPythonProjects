import turtle
t = turtle.Pen()
t.width(3)

n = int(input("Enter here. : "))
x = int(input("Enter here. : "))

t.up()
t.backward(300)
t.down()

if (x < 6):
    for num in range (x):
        for i in range (n):
            t.forward(25)
            t.left(360/n)
        t.up()
        t.forward(150)
        t.down()
if (x > 6):
    for num in range (5):
        for i in range (n):
            t.forward(25)
            t.left(360/n)
        t.up()
        t.forward(150)
        t.down()
    t.up()
    t.goto(-300,-200)
    t.down()
    for num in range (x - 5):
        for i in range (n):
            t.forward(25)
            t.left(360/n)
        t.up()
        t.forward(150)
        t.down()
    
