import random
import turtle
t = turtle.Pen()
t.width(3)
t.speed(0)

t.up()
t.goto(-250,-200)
t.down()

for number in range (3):
    for y in range (5):
        for i in range (6):
            for x in range (8):
                t.pencolor (random.random (), random.random (), random.random ())
                t.left(45)
                t.forward(25)
            t.left(360/6)
        t.up()
        t.forward(100)
        t.down()
    t.up()
    t.left(120)
    t.forward(100)
    t.down()  
            
            
