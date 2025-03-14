#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    num_returned = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            num_returned += 1
        except IndexError as IE:
            break
    print()
    return num_returned
=======
    num = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            num += 1
        except IndexError:
            break
    print()
    return num
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
