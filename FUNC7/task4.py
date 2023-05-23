import random

def get_random_array(n):
    numbers = []
    for i in range (n):
        numbers.append(random.randint(1,10))
    return (numbers)

def reverse(array):
    array = array[::-1]
    return (array)

array = get_random_array(int(input("Enter a number: ")))
print (array)
print (reverse(array))
