numbers = [int(i) for i in input().split()]
num = 0
i = 0
for number in numbers:
    if (i % 2 == 0):
        num += number
    i += 1
print (num * numbers[0])
