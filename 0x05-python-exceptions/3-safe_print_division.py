#!/usr/bin/python3
def safe_print_division(a, b):
    quot = 0
    try:
        quot = a / b
    except (ZeroDivisionError):
        quot = None
    finally:
        print("Inside result: {}".format(quot))
        return quot
