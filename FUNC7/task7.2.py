import random

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

def get_lucky():
    lucky = ""
    for i in range (6):
        lucky += str(random.randint(0,10))
    if (detect_lucky(lucky)):
        return int(lucky)
    else:
        return get_lucky()


print (get_lucky())
