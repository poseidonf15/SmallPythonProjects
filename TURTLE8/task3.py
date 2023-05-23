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

def increase ():
    global speed
    speed += 5

def decrease ():
    global speed
    speed -= 5

def Space ():
    global press
    if (press % 2 == 0):
        a.hideturtle()
    else:
        a.showturtle()
    press += 1

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.onkeypress(increase,"q")
turtle.onkeypress(decrease,"w")
turtle.onkeypress(Space,"space")
turtle.listen()
