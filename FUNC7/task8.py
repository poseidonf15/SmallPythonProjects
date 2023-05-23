def average(numbers):
    num = 0
    for number in numbers:
        num += number
    return (num / len(numbers))

print (average([int(i) for i in input().split()]))
