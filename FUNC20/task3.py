def multiply (numbers):
    x = 1
    for number in numbers:
        x = x * number
    return x
print (multiply(input().split()))
