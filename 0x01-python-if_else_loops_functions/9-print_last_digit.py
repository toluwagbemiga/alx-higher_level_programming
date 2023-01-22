#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    num1 = number % 10
    print("{}".format(num1), end='')
    return num1
