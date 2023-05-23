import turtle
a = turtle.Pen()
a.speed(0)

a.right(90)
a.color("red","red")
a.up()
a.goto(0,200)
a.down()

x1 = 0
y1 = 180
x2 = 0
y2 = 0
l = 20

for i in range(10):
    a.goto(x2,y2)
    a.up()
    a.goto(x1,y1)
    a.down()
    x2 += 20
    y1 -= 20

for i in range(10):
    a.goto(x2,y2)
    a.up()
    a.goto(x1,y1)
    a.down()
    x2 -= 20
    y1 -= 20

y1 += 40

for i in range(10):
    a.goto(x2,y2)
    a.up()
    a.goto(x1,y1)
    a.down()
    x2 -= 20
    y1 += 20
    
for i in range(10):
    a.goto(x2,y2)
    a.up()
    a.goto(x1,y1)
    a.down()
    x2 += 20
    y1 += 20

    


    
    
    
