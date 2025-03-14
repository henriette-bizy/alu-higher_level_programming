#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
<<<<<<< HEAD
        return True
    except (TypeError, ValueError):
        return False
=======
    except:
        return False
    return True
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
