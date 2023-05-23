def sum_of_digits(numbers):
    num = 0
    for number in range (0, len(numbers)):
        num += int(numbers[number])
    return num

x1name = input("First number: ")
x2name = input("Second number: ")
x1 = sum_of_digits(x1name)
x2 = sum_of_digits(x2name)

if (x1 > x2):
    print (f"Sum of the digits in {x1name} is greater")
elif (x2 > x1):
    print (f"Sum of the digits in {x2name} is greater")
else:
    print (f"Sum of the digits in {x2name} and {x1name} are eqales")
