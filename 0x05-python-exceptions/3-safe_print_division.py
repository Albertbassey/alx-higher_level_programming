#!/usr/bin/python3

def safe_print_division(c, d):
    try:
        result = c / d

    except ZeroDivisionError:

        result = None

    finally:
        print("Inside result: {}".format(result))
    return(result)
