def factorial(n):
    num = 1
    for i in range (1,n+1):
        num *= i
    return (num)

print (2*factorial(5)+3*factorial(8)/factorial(6)+factorial(4))
