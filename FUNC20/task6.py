def check(numbers):
    if (numbers[1] > numbers[0] and numbers[1] < numbers[2]):
        print ("The number is in the right range")
    elif (numbers[1] < numbers[0] and numbers[1] > numbers[2]):
        print (f"""{numbers[1]} is smaller than {numbers[0]}
and biger than {numbers[2]}
so the number is not in the right range""")
    elif (numbers[1] < numbers[0]):
        print (f"""{numbers[1]} is smaller than {numbers[0]}
so he is not in the right range""")
    else:
        print (f"""{numbers[1]} is biger than {numbers[2]}
so the number is not in the right range""")

check(input().split())
