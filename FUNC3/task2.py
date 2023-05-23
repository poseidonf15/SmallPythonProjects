def change (my_list):
    my_list = [*my_list[2:], *my_list[0:2]]
    return my_list
print (change([1, 2, 3, 4, 5, 6]))
