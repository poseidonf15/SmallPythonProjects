import turtle
a = turtle.Pen()
a.width(3)

press = 0
speed = 20

def up ():
    global speed
    x,y = a.pos()
    a.goto(x, y + speed)

def down ():
    global speed
    x,y = a.pos()
    a.goto(x, y - speed)

def left ():
    global speed
    x,y = a.pos()
    a.goto(x - speed, y)

def right ():
    global speed
    x,y = a.pos()
    a.goto(x + speed, y)

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()
