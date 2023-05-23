import turtle

a = turtle.Pen()

a.speed(0)
a.color("black","yellow")

def pyramid(n,k):
    if (k <= 0):
        return (k)
    else:
        a.width(k)
        a.begin_fill()
        for i in range(6):
            a.forward(n)
            a.left(60)
        a.end_fill()
        a.up()
        a.forward(10)
        a.left(90)
        a.forward(40)
        a.right(90)
        a.down()
        return (100)

n = int(input(": "))
k = int(input(": "))

a.up()
a.goto(n / 2 * -1, n / 2 * -1)
a.down()

while(True):
    x = pyramid(n,k)
    n -= 20
    k -= 1
    if (x <= 0):
        break
    
            
