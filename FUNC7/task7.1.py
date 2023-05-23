def detect_lucky(numbers):
    a = 0
    b = 0
    for i in range (0,3):
        a += int(numbers[i])
    for i in range (3,6):
        b += int(numbers[i])
    if (a == b):
        return True
    else:
        return False

print (detect_lucky(input("Enter a six-digit number: ")))
