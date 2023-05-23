def sum_of_digits(numbers):
    num = 0
    for number in range (0, len(numbers)):
        num += int(numbers[number])
    return num

print (sum_of_digits((input("Enter a number: "))))
