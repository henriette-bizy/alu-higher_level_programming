#!/usr/bin/python3
def safe_print_division(a, b):
    try:
<<<<<<< HEAD
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
        return quotient
=======
        try:
            result = a / b
            print("Inside result: {}".format(result))
        except:
            result = None
            print("Inside result: {}".format(result))
    finally:
        return result
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
