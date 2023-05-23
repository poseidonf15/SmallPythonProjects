def find_speed(kilometers, hours):
    meters = kilometers * 1000
    seconds = hours * 3600
    return (meters / seconds // 0.01 / 100)
print (find_speed(100, 3))
