import turtle
a = turtle.Pen()
a.width(5)
a.speed(0)
a.hideturtle()

x = -50
x2 = 50
y = -75
num = 0
num2 = 0

a.up()
a.goto(x,y)
a.down()
a.goto(num,num2)

a.up()
a.goto(x2,y)
a.down()
a.goto(num,num2)

a.left(90)
a.forward(50)

a.left(140)
a.forward(50)
a.backward(50)

a.right(280)
a.forward(50)
a.backward(50)

a.left(50)
a.begin_fill()
a.circle(25)
a.end_fill()

def left():
    global x
    global x2
    global y
    global num
    global num2
    
    a.clear()
    x = x - 10
    x2 = x2 - 10
    num = num - 10

    a.up()
    a.goto(x,y)
    a.down()
    a.goto(num,num2)

    a.up()
    a.goto(x2,y)
    a.down()
    a.goto(num,num2)

    a.left(90)
    a.forward(50)

    a.left(140)
    a.forward(50)
    a.backward(50)

    a.right(280)
    a.forward(50)
    a.backward(50)

    a.left(50)
    a.begin_fill()
    a.circle(25)
    a.end_fill()

def right():
    global x
    global x2
    global y
    global num
    global num2
    
    a.clear()
    x = x + 10
    x2 = x2 + 10
    num = num + 10

    a.up()
    a.goto(x,y)
    a.down()
    a.goto(num,num2)

    a.up()
    a.goto(x2,y)
    a.down()
    a.goto(num,num2)

    a.left(90)
    a.forward(50)

    a.left(140)
    a.forward(50)
    a.backward(50)

    a.right(280)
    a.forward(50)
    a.backward(50)

    a.left(50)
    a.begin_fill()
    a.circle(25)
    a.end_fill()

def up():
    global x
    global x2
    global y
    global num
    global num2
    
    a.clear()
    y = y + 10
    num2 = num2 + 10
    
    a.up()
    a.goto(x,y)
    a.down()
    a.goto(num,num2)

    a.up()
    a.goto(x2,y)
    a.down()
    a.goto(num,num2)

    a.left(90)
    a.forward(50)

    a.left(140)
    a.forward(50)
    a.backward(50)

    a.right(280)
    a.forward(50)
    a.backward(50)

    a.left(50)
    a.begin_fill()
    a.circle(25)
    a.end_fill()

def down():
    global x
    global x2
    global y
    global num
    global num2
    
    a.clear()
    y = y - 10
    num2 = num2 - 10

    a.up()
    a.goto(x,y)
    a.down()
    a.goto(num,num2)

    a.up()
    a.goto(x2,y)
    a.down()
    a.goto(num,num2)

    a.left(90)
    a.forward(50)

    a.left(140)
    a.forward(50)
    a.backward(50)

    a.right(280)
    a.forward(50)
    a.backward(50)

    a.left(50)
    a.begin_fill()
    a.circle(25)
    a.end_fill()

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()




























    
