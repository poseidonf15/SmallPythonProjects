line = input("Enter your line. : ")
find = line.find(" ")
x = len(line[0:find])
i = 0
i2 = x + 1
num = 0

while (i < x):
    if (line[i] == line[i2]):
        num += 1
    else:
        break
    i += 1
    i2 += 1
print (num)
