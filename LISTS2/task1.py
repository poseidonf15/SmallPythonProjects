letters = input().split()
num = len(letters)
if (num % 2 != 0):
    print (letters[0] , letters[num // 2] , letters[-1])
else:
    print (letters[0] , letters[num // 2 - 1] , letters [num // 2] , letters[-1])
