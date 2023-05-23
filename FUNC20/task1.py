def num (numbers):
    x = numbers[0]
    numbers = numbers[1:]
    for number in numbers:
        if (number > x):
            x = number
    return x
print (num(input().split()))
