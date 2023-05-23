numbers = [int(i) for i in input().split()]
n = int(input())
x = 9999
y = 9999
x2 = 10000
y2 = 10000

for number in numbers:
    if (n - number > 0):
        x2 = n - number
    if (number - n > 0):
        y2 = number - n
    if (x > x2):
        x = x2
        xx = number
    if (y > y2):
        y = y2
        yy = number

if (y < x):
    print (yy)
elif (x < y):
    print (xx)
elif (xx < yy):
    print (xx)
else:
    print (yy)
    
    
