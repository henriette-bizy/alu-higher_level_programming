#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
<<<<<<< HEAD
    new_list = []
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            new_list.append(quotient)
    return new_list
=======
    results = []
    try:
        for i in range(list_length):
            try:
                results.append(my_list_1[i] / my_list_2[i])
            except TypeError:
                print("wrong type")
                results.append(0)
            except ZeroDivisionError:
                print("division by 0")
                results.append(0)
            except IndexError:
                print("out of range")
                results.append(0)
    finally:
        return results
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
