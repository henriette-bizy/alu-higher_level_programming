#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
<<<<<<< HEAD
        if (i % 3) == 0 and (i % 5) == 0:
=======
        if i % 3 == 0 and i % 5 == 0:
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
