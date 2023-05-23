num = 0
count = 0
while (num >= 0):
    num = float(input("Enter the price : "))
    if (num >= 1000):
        count += num - 5 * num / 100
    else:
        count += num
count -= num
print (f"You need to pay {count}$")
