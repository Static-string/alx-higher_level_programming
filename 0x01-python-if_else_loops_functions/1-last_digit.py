#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    mod_num = number % 10
    if mod_num >= 6:
        print("Last digit of {:d} is {:d} and is greater than 5"
                .format(number, mod_num))
    elif mod_num > 0 & mod_num < 6:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
                    .format(number, mod_num))
    else:
        print("Last digit of {:d} is 0 and is 0".format(number))

if number < 0:
    pos_num = number * -1
    mod_pos_num = pos_num % 10
    if mod_pos_num != 0:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
                    .format(number, mod_pos_num * -1))
    else:
        print("Last digit of {:d} is 0 and is 0".format(number))
if number == 0:
    print("Last digit of 0 is 0 and is 0")
