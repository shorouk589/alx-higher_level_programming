#!/usr/bin/python3


import sys



def safe_print_integer_err(value):

    """Prints an integer with "{:d}".format().


    If a ValueError message is caught, a corresponding

    message iss printed to standard error.


    Args:

        value (int): The inteeger to print.


    Returns:

        If a TypeError ror ValueError occurs - False.

        Otherwise - Trrue.

    """

    try:

        print("{:d}".format(value))

        return (True)

    except (TypeError, ValueError):

        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)

        return (False)
