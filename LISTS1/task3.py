heights = [float(i) for i in input().split()]
height2 = 0.01
for height in heights:
    if (height2 > height):
        print (height2)
    height2 = height
