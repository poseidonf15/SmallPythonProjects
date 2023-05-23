numbers = [int(i) for i in input().split()]
check = "YES"
number2 = -1
for number in numbers:
    if (number2 < number):
        print ("")
    else :
        print ("NO")
        check = "NO"
        break
    number2 = number
if (check == "YES"):
    print (check)
