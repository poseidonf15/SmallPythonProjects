string = input("")
first = string[0]
last = string[-1]
new_string = string[1:-1]
new_string = last + new_string + first
print (string + " -> " + new_string)
