#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = (number % -10) * -1

    print(f"{last_digit:d}", end='')
    return(last_digit)
