def factorial(number):
    for i in range (1,number):
        number = number * i
    return number
print (factorial(int(input())))
