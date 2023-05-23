import random

def get_random_array(n = 10):
    numbers = []
    for i in range (n):
        numbers.append(random.randint(1,10))
    print (numbers)
n = input("Enter a number: ")
if (n.isnumeric()):
    get_random_array(int(n))
else:
    get_random_array()



    
