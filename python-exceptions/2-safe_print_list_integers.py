#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
<<<<<<< HEAD
    num_returned = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_returned += 1
        except(TypeError, ValueError):
            pass
    print()
    return num_returned
=======
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except(TypeError, ValueError):
            continue
    print()
    return num
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
